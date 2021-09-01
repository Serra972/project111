import statistics as st
import pandas as pd
import csv
import random
import plotly.figure_factory as ff
import plotly.graph_objects as go
df=pd.read_csv("data1.csv")
data=df["claps"].tolist()
population_mean=st.mean(data)
population_stdev=st.stdev(data)
print(population_stdev,population_mean)
def random_set_mean(counter):
    dataset=[]
    for i in range(0,100):
        random_index=random.randint(0,len(data)-1)
        value=data[random_index]
        dataset.append(value)
    mean=st.mean(dataset)
    return(mean)
meanlist=[]
for i in range (0,1000):
    setofmeans=random_set_mean(100)
    meanlist.append(setofmeans)
st_dev=st.stdev(meanlist)
fstdstart,fstdend=population_mean-population_stdev,population_mean+population_stdev
sstdstart,sstdend=population_mean-(2*population_stdev),population_mean+(2*population_stdev)
tstdstart,tstdend=population_mean-(3*population_stdev),population_mean+(3*population_stdev)
print(fstdstart,fstdend,sstdstart,sstdend,tstdstart,tstdend)
graph=ff.create_distplot([meanlist],["temp"],show_hist=False)
graph.add_trace(go.Scatter(x=[population_mean,population_mean],y=[0,0.2],mode="lines",name="mean"))
graph.add_trace(go.Scatter(x=[fstdstart,fstdstart],y=[0,0.2],mode="lines",name="mean"))
graph.add_trace(go.Scatter(x=[fstdend,fstdend],y=[0,0.2],mode="lines",name="mean"))
graph.add_trace(go.Scatter(x=[sstdstart,sstdstart],y=[0,0.2],mode="lines",name="mean"))
graph.add_trace(go.Scatter(x=[sstdend,sstdend],y=[0,0.2],mode="lines",name="mean"))
graph.add_trace(go.Scatter(x=[tstdstart,tstdstart],y=[0,0.2],mode="lines",name="mean"))
graph.add_trace(go.Scatter(x=[tstdend,tstdend],y=[0,0.2],mode="lines",name="mean"))

df=pd.read_csv("data1.csv")
data=df["claps"].tolist()
sample_mean=st.mean(data)
graph.add_trace(go.Scatter(x=[sample_mean,sample_mean],y=[0,0.2],mode="lines",name="mean"))
graph.show()
zcore=(sample_mean-population_mean)/population_stdev
print(zcore)