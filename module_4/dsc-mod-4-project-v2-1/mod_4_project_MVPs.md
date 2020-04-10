# MVPs for Mod 4 Project

## Reminder: what is an MVP?

An MVP is a "minimum viable product".  It's the minimal amount of work that can be said to have completed the requirements.  This is a ubiquotous idea in the business world, and it's useful to have as a scheduling / workflow target to hit.  

The idea is: 
- figure out what your "minimum viable product" would be for your task.  In this case, the question to ask yourself is "what's the minimum amount of work I could do that would enable me to provide an answer to the question I'm investigating with the data I'm using?"

- only do work that completes the MVP; if a given task doesn't help you complete the MVP, don't do it

- once you complete the MVP, if you have time remaining, you can add on to your work to make it better

This is partially why we help you design your projects so that they're modular: a project that has an MVP stage + additional work to make it better is more likely to be completed on time than a project that is structured in an "all-or-nothing" way.




## When do I need to have an "MVP" completed by?

Wednesday 1pm.  Get crackin!




## What is an 'MVP' for this mod project?

In previous mods, MVPs have been 3 EDA graphs and comparisons of at least two models using appropriate metrics.  For some of this mod's projects, MVPs will run a little differently.  

### Time Series

Because time series models are similar to the models you worked with in previous mods and are quick to run, an MVP of a time series model is the same as an MVP in previous mods: 3 EDA graphs and comparisons of two models using appropriate metrics.


### Neural Nets

Neural net MVPs will be a bit different.  Because they take so long to run, just having fit one model and reporting the available metric it's optimizing (accuracy, etc.) will be sufficient.  

If the data you're using for NNs is amenable to EDA (eg, text data), you'll be expected to also provide the typical 3 EDA graphs.  However, if your data is something like images where the typical EDA process doesn't make sense, you'll be expected to explain your data preprocessing steps in more detail.  How do you translate the images into data that the NN can use?  What sorts of preprocessing steps do you do on that data before feeding it into the NN (eg, standardizing the color scheme) and why?  Etc. 

You will also be expected to explain a bit more in detail why you chose that particular neural network architecture to use for your task, and what that architecture is doing. Why did you choose the number and structure of layers that you did?  If you included specific techniques eg pooling or regularization, why did you do so?   Etc.  

### Recommendation systems

Because recommendation systems are harder to produce comparison metrics for, the MVP will just be "a working recommendation system": provide a recommendation that satisfies the use case you built your recommendation system for.  Eg, if you're doing a movie recommender, demonstrate that your system can provide a recommendation for a new user.

Like with NNs, you'll be expected to explain more about what calculations your model is doing, and why you chose those calculations specifically.  

Also like with NNs, the typical EDA process doesn't make much sense.  Instead, you'll be asked to speak through how your use case and the structure of your data inform why you chose your particular approach to constructing a recommendation system.  How did you make your choice between a content or collaborative system?  Does your data not have a lot of user ratings, and so you chose an item-item system?  Is your use case trying to match people together, and so you chose a user-user system?  Why did you chose your specific calculations to generate recommendations?  Etc.