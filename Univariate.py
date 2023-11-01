class Univariate():
    def quanqual(dataset):
        quantitative=[]
        qualitative=[]
        for i in dataset.columns:
            #print(i)
            if(dataset[i].dtype=='O'):
                #print('quantitative')
                quantitative.append(i)
            else:
                #print('qualitative')
                qualitative.append(i)
        return quantitative,qualitative