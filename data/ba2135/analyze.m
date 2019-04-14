anchordata = readtable('anchordata.csv');
tag0posa = readtable('pos_a.csv');
tag0posb = readtable('pos_b.csv');
tag0posc = readtable('pos_c.csv');
tag0posd = readtable('pos_d.csv');
tag0pose = readtable('pos_e.csv');

true_a = [3.75;2.63];
true_b = [2.25;5.63];
true_c = [9.75;2.63];
true_d = [11.25;7.13];
true_e = [11.15;1.75];

distances = [];
rssi = [];

for i=1:size(tag0posa, 1)
    anchorIndex = find(anchordata.anchorId == tag0posa(i, :).anchorId);
    anchorPos = [anchordata(anchorIndex, :).X;anchordata(anchorIndex, :).Y];
    distances = [distances; norm(anchorPos - true_a)];
    rssi = [rssi; tag0posa.rssi(i)];
end
for i=1:size(tag0posb, 1)
    anchorIndex = find(anchordata.anchorId == tag0posb(i, :).anchorId);
    anchorPos = [anchordata(anchorIndex, :).X;anchordata(anchorIndex, :).Y];
    distances = [distances; norm(anchorPos - true_b)];
    rssi = [rssi; tag0posb.rssi(i)];
end
for i=1:size(tag0posc, 1)
    anchorIndex = find(anchordata.anchorId == tag0posc(i, :).anchorId);
    anchorPos = [anchordata(anchorIndex, :).X;anchordata(anchorIndex, :).Y];
    distances = [distances; norm(anchorPos - true_c)];
    rssi = [rssi; tag0posc.rssi(i)];
end
for i=1:size(tag0posd, 1)
    anchorIndex = find(anchordata.anchorId == tag0posd(i, :).anchorId);
    anchorPos = [anchordata(anchorIndex, :).X;anchordata(anchorIndex, :).Y];
    distances = [distances; norm(anchorPos - true_d)];
    rssi = [rssi; tag0posd.rssi(i)];
end
for i=1:size(tag0pose, 1)
    anchorIndex = find(anchordata.anchorId == tag0pose(i, :).anchorId);
    anchorPos = [anchordata(anchorIndex, :).X;anchordata(anchorIndex, :).Y];
    distances = [distances; norm(anchorPos - true_e)];
    rssi = [rssi; tag0pose.rssi(i)];
end

scatter(distances, rssi)