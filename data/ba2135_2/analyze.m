anchordata = readtable('anchordata.csv');
tag0posc = readtable('pos_c.csv');

true_a = [3.75;2.63];
true_b = [2.25;5.63];
true_c = [9.75;2.63];
true_d = [11.25;7.13];
true_e = [11.15;1.75];

distances = [];
rssi = [];


for i=1:size(tag0posc, 1)
    anchorIndex = find(anchordata.anchorId == tag0posc(i, :).anchorId);
    anchorPos = [anchordata(anchorIndex, :).X;anchordata(anchorIndex, :).Y];
    distances = [distances; norm(anchorPos - true_c)];
    rssi = [rssi; tag0posc.rssi(i)];
end

scatter(distances, rssi)