% Load data from the CSV file
filename = 'parking_srv_to_botanic_grdn.csv'; % Input CSV file
data = readtable(filename); % Read the data into a MATLAB table

% Extract relevant data from the CSV
latitudes = data.lat; % Latitude coordinates of the UE
longitudes = data.lon; % Longitude coordinates of the UE
cellIDs = data.cellid; % Cell tower IDs connected to the UE
signalStrength = data.signal; % Signal strength in dBm (decibel-milliwatts)
radiotype = data.radiotype; % Network type (e.g., "5G (NSA)")

% Smooth signal strength to reduce noise
windowSize = 2; % Smaller window size ensures less aggressive smoothing
smoothedSignal = movmean(signalStrength, windowSize); % Apply moving average

% Parameters for handover simulation
handoverThreshold = -120; % Signal strength threshold (dBm) for poor connection
minHandoverGap = 8; % Minimum number of indices to prevent frequent handovers

% Define gNB (base station) parameters using the 5G Toolbox
gnbConfig = struct();
gnbConfig.Position = [ % gNB geographical coordinates (close to UE trajectory)
    -117.3207, 33.9777;  % gNB1 (Longitude, Latitude)
    -117.3217, 33.9759   % gNB2 (Longitude, Latitude)
];
gnbConfig.Power = [20, 20]; % Transmit power for each gNB (dBm)
gnbConfig.Frequency = 3.5e9; % Carrier frequency in Hz

% Compute distance-based signal strength for each gNB using a simple path loss model
gnbConfig.SignalStrength = zeros(height(data), size(gnbConfig.Position, 1));
for i = 1:size(gnbConfig.Position, 1)
    % Distance between UE and gNB
    gnbDist = sqrt((longitudes - gnbConfig.Position(i, 1)).^2 + ...
                   (latitudes - gnbConfig.Position(i, 2)).^2);
    % Free-space path loss model with fixed constant for realistic scaling
    gnbConfig.SignalStrength(:, i) = gnbConfig.Power(i) - ...
        20 * log10(gnbDist + 1) - 20 * log10(gnbConfig.Frequency) - 147.55 + 100;
end

% Combine signals from all gNBs
combinedSignal = max(gnbConfig.SignalStrength, [], 2); 
smoothedSignal5GToolbox = movmean(combinedSignal, windowSize);

% Detect Actual 5G-to-5G Handovers (from CSV)
previousRadiotype = [""; radiotype(1:end-1)]; % Track previous radiotype
actualHandovers = find([false; diff(cellIDs) ~= 0] & ...
                       strcmp(radiotype, '5G (NSA)') & ...
                       strcmp(previousRadiotype, '5G (NSA)'));

% Simulate Handovers (5G Toolbox-based signal strength)
simulatedHandovers = [];
lastHandoverIndex = -inf; % Track the last handover index

for i = 2:height(data)
    % Handover logic checks signal strength and radiotype continuity
    if combinedSignal(i) < handoverThreshold && ...
       strcmp(radiotype(i), '5G (NSA)') && ...
       strcmp(radiotype(i-1), '5G (NSA)') && ...
       (i - lastHandoverIndex > minHandoverGap)
        simulatedHandovers = [simulatedHandovers; i];
        lastHandoverIndex = i; % Update last handover index
    end
end

% Calculate overlap between actual and simulated handovers
overlapIndices = arrayfun(@(x) find(abs(simulatedHandovers - x) <= 1, 1, 'first'), actualHandovers, 'UniformOutput', false);

% Filter out empty results from overlapIndices
validOverlaps = ~cellfun(@isempty, overlapIndices);
overlapIndices = cell2mat(overlapIndices(validOverlaps)); % Convert valid overlaps to numeric array

% Map Video Quality Based on Signal Strength
videoQualityLevels = zeros(size(smoothedSignal));
for i = 1:length(smoothedSignal)
    if smoothedSignal(i) >= -70
        videoQualityLevels(i) = 4; % Ultra HD (4K)
    elseif smoothedSignal(i) >= -85
        videoQualityLevels(i) = 3; % Full HD (1080p)
    elseif smoothedSignal(i) >= -100
        videoQualityLevels(i) = 2; % Standard HD (720p)
    else
        videoQualityLevels(i) = 1; % Low Resolution (480p)
    end
end

% Visualization 1: Simulated vs Actual Handovers
figure;
plot(longitudes, latitudes, '-o', 'DisplayName', 'UE Trajectory', 'Color', 'blue'); hold on;

% Plot Actual Handovers
scatter(longitudes(actualHandovers), latitudes(actualHandovers), 200, 'r', '*', ...
    'LineWidth', 2, 'DisplayName', 'Actual Handovers');

% Plot Simulated Handovers
scatter(longitudes(simulatedHandovers), latitudes(simulatedHandovers), 150, 'm', 'd', ...
    'LineWidth', 1.5, 'DisplayName', 'Simulated Handovers');

% Highlight Overlaps
scatter(longitudes(actualHandovers(validOverlaps)), latitudes(actualHandovers(validOverlaps)), 300, 'k', 'o', ...
        'LineWidth', 2, 'DisplayName', 'Overlap (Actual vs Simulated)');

xlabel('Longitude');
ylabel('Latitude');
title('Simulated vs Actual Handovers with Overlaps Highlighted');
legend('show');
grid on;

% Visualization 2: Video Quality Changes During Handovers
figure;
plot(1:height(data), videoQualityLevels, '-o', 'DisplayName', 'Video Quality Over Time', 'Color', [1, 0.5, 0], 'LineWidth', 1.5);
hold on;

% Mark actual handovers on the video quality graph
scatter(actualHandovers, videoQualityLevels(actualHandovers), 150, 'r', '*', ...
    'LineWidth', 2, 'DisplayName', 'Actual Handovers');

% Mark simulated handovers on the video quality graph
scatter(simulatedHandovers, videoQualityLevels(simulatedHandovers), 150, 'm', 'd', ...
    'LineWidth', 1.5, 'DisplayName', 'Simulated Handovers');

% Enhance readability with labels and legends
xlabel('Time (Steps)');
ylabel('Video Quality');
yticks([1, 2, 3, 4]);
yticklabels({'Low Resolution (480p)', 'Standard HD (720p)', 'Full HD (1080p)', 'Ultra HD (4K)'});
title('Video Quality Changes During Handovers');
legend('show');
grid on;
