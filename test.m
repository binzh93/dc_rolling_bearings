% 时频分析
clc;
clear ;
OtpDir1 = '/Users/harudaee/Documents/MATLAB/zhoucheng/test_file/test/';%输出路径
load test.mat%加载数据
s=zeros(1,1200);
[m,n]=size(data_test);%要修改
totalscal=256;
k=1;
% 原始信号
fs=12000;
t=0:(1/fs):(0.1-1/fs);
for i=1:1:m
    for j=1:1200:4801
    close all;    
       s = data_test(i,j:j+1199);%每次读取矩阵一行的一部分 .  要修改
       wavename='cmor3-3';
       Fc=centfrq(wavename); % 小波的中心频率
       c=2*Fc*totalscal;
       scals=c./(1:totalscal);
       f=scal2frq(scals,wavename,1/fs); % 将尺度转换为频率
       coefs=cwt(s,scals,wavename); % 求连续小波系数
       figure;
       imagesc(t,f,abs(coefs));
       set(gca,'YDir','normal');
       colorbar;
       xlabel('时间 t/s');
       ylabel('频率 f/Hz');
       title('小波时频图');
        close(figure); %关闭figure，清空内存
        ff=getframe(gcf);
         newname=sprintf('test_%d',k);%%要修改
        imwrite(ff.cdata,[OtpDir1,newname,'.jpg']);
        k=k+1;
    end
end





    