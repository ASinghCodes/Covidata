The data used here is from the World Health Organization (WHO)
Data can be found here directly:
https://www.who.int/data/sets/global-excess-deaths-associated-with-covid-19-modelled-estimates

Disclaimer: some column names were changed due to ease of use, for example: excess.mean -> excess_mean and so forth

Dependency needed: matplotlib, seaborn, pandas, openpyxl

------------------------------------------------------------
When I started this project I had the hypothesis that lower income countries would see a higher number of excess deaths than their respective counterparts. 

After cleaning out and visualizing the data this turned out not to be the case, to a degree.

From using seaborn visualization I was able to note the following:

1) Excess deaths did drop after the initial year of COVID-19, this is likely due to the lockdowns, natural immunization, and the vaccine being released in 2021.

2) While Low-Income countries has the highest spike in excess deaths as designated by figure 2, that spike showcases the count of excess deaths at that range, so while they had the most excess deaths in that small range, they did NOT have the most deaths overall and this was more easily seen through Tableau 

After transfering the data to a csv file and creating a dashboard on Tableau, Figure 4, data further become clear in showcasing that the leader in most excess deaths were the Lower-Middle countries, and to my surprise Low-Income countries was the least in excess deaths.

My assumptions as to why this could be are as follows:

1) Low-Income countries in this dataset have higher expected death rates comparitively to non Low-Income countries. For this I would need to be provided a dataset column of expected occupency. Using this I could draw a percentage viewpoint and compare it to naturally higher occupancy countries.

2) As stated briefly in point a, the overall size of a Low-Income countries plays a role. Lower density would usually mean less people to spread the virus to. Fewer infections also means fewer possible chances of mutations, which in turn would make the vaccine more effective at irradication.

Regardless, to get a further clean understanding of why this data is as such, I would need access to more in depth information. Ideally I would have a data set that showcases all countries excess deaths by month and year, total population, when the vaccine was first available to them/how many people were vaccinated for that month of reporting, and so forth.

For now I will put this project to rest and may expand on it in the future with a much more in depth dataset. 

![Figure 1](https://github.com/ASinghCodes/Covidata/blob/50c6e173e65b33ec45c8e5220e7637c1ba24ebc5/Figure_1.png)

![Figure 2](https://github.com/ASinghCodes/Covidata/blob/50c6e173e65b33ec45c8e5220e7637c1ba24ebc5/Figure_2.png)

![Figure 3](https://github.com/ASinghCodes/Covidata/blob/50c6e173e65b33ec45c8e5220e7637c1ba24ebc5/Figure_3.png)

![Figure 4](https://github.com/ASinghCodes/Covidata/blob/afb4d20676ce7ba574d4fd2d175668407cb1526e/Figure_4.PNG)
