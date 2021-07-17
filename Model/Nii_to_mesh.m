load path.mat
test = loadnifti(path);

clear opt
for n = 1:max(test.NIFTIData(:))
    opt(n).keepratio=0.1;
    opt(n).radbound=2;
    opt(n).side='lower';
end

[node,elem,face]=vol2mesh(test.NIFTIData,1:size(test.NIFTIData,1),1:size(test.NIFTIData,2),1:size(test.NIFTIData,3),opt,100,1);
for n = 1:max(elem(:,5))
    fc1=volface(elem(elem(:,5)==n,1:4));
    filename1 = ['./niistlfile/',num2str(n), ".stl"];
    savestl(node,fc1,filename1)
end
