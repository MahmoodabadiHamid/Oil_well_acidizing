library(bnlearn)
a=X022_preprocessing_after_normalizing_values[,-c(1,21,24)]
aa=X011_preprocessing_after_encoding_label
aaa=Sample_Synthetic_Data_Revised
#b=empty.graph(names(a))
#plot(b)
plot(gs(a))
g=bn.fit(gs(a),a)
#mmhc
plot(mmhc(a))
m=bn.fit(mmhc(a),a)
coef(m)
#modelstring(c)
plot(hc(a))
h=bn.fit(hc(a),a)
arcs(h)
coef(h)
modelstring(h)
nparams(h)
h=plot(hc(a))
#as.data.frame()
#is.data.frame(a)
all.equal(g,h)
write.csv(arcs(h),"E:/company/python/Oil_well_acidizing/Dataset/Second Dataset/Arc.csv")
