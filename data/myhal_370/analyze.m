anchordata = readtable('anchordata.csv');
tag0posa = readtable('tag0_pos_a.csv');
tag0posb = readtable('tag0_pos_b.csv');
tag0posc = readtable('tag0_pos_c.csv');
tag0posd = readtable('tag0_pos_d.csv');
tag0pose = readtable('tag0_pos_e.csv');
tag0posf = readtable('tag0_pos_f.csv');
tag0posg = readtable('tag0_pos_g.csv');
tag0posh = readtable('tag0_pos_h.csv');
tag0posi = readtable('tag0_pos_i.csv');
tag0posk = readtable('tag0_pos_k.csv');

true_a = [0.35;2.72];
true_b = [0.15;5.12];
true_c = [1.59;8.48];
true_d = [3.51;8.95];
true_e = [2.07;5.60];
true_f = [4.47;5.60];
true_g = [6.87;6.08];
true_h = [5.91;8.48];
true_i = [4.47;3.20];
true_j = [3.51;1.28];
true_k = [7.35;1.76];

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
for i=1:size(tag0posf, 1)
    anchorIndex = find(anchordata.anchorId == tag0posf(i, :).anchorId);
    anchorPos = [anchordata(anchorIndex, :).X;anchordata(anchorIndex, :).Y];
    distances = [distances; norm(anchorPos - true_f)];
    rssi = [rssi; tag0posf.rssi(i)];
end
for i=1:size(tag0posg, 1)
    anchorIndex = find(anchordata.anchorId == tag0posg(i, :).anchorId);
    anchorPos = [anchordata(anchorIndex, :).X;anchordata(anchorIndex, :).Y];
    distances = [distances; norm(anchorPos - true_g)];
    rssi = [rssi; tag0posg.rssi(i)];
end
for i=1:size(tag0posh, 1)
    anchorIndex = find(anchordata.anchorId == tag0posh(i, :).anchorId);
    anchorPos = [anchordata(anchorIndex, :).X;anchordata(anchorIndex, :).Y];
    distances = [distances; norm(anchorPos - true_h)];
    rssi = [rssi; tag0posh.rssi(i)];
end
for i=1:size(tag0posi, 1)
    anchorIndex = find(anchordata.anchorId == tag0posi(i, :).anchorId);
    anchorPos = [anchordata(anchorIndex, :).X;anchordata(anchorIndex, :).Y];
    distances = [distances; norm(anchorPos - true_i)];
    rssi = [rssi; tag0posi.rssi(i)];
end
for i=1:size(tag0posk, 1)
    anchorIndex = find(anchordata.anchorId == tag0posk(i, :).anchorId);
    anchorPos = [anchordata(anchorIndex, :).X;anchordata(anchorIndex, :).Y];
    distances = [distances; norm(anchorPos - true_k)];
    rssi = [rssi; tag0posk.rssi(i)];
end


scatter(distances, rssi)