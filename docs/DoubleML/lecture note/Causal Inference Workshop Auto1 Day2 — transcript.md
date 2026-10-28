# Causal Inference Workshop Auto1, Day 2 (6 Mar 2026) — transcript

> Extracted from `Causal Inference Workshop Auto1 Day2 - 2026_03_06 09_20 CET - Notes by Gemini.pdf`
> Google Meet / Gemini export of the Causal Inference Workshop Auto1, Day 2 (6 Mar 2026) session.

Mar 6, 2026 Causal Inference Workshop Auto1 Day2 - Transcript

### 00:00:00

**Martin Bierey:** Hey, good

**Leon Ostermann:** All right.

**Sven Klaassen:** All right.

**Martin Spindler:** Hello.

**Daniel Jacob:** Hello. Hello. Good morning everyone.

**Martin Spindler:** Hello. Good morning.

**Sven Klaassen:** Are

**Leon Ostermann:** Yeah.

**Tsz Yan Lam:** Funny.

**Ruizhe Chao:** Her

**Sven Klaassen:** you

**Jan Rabenseifner:** Morning.

**Martin Spindler:** Morning.

**Ani Pole:** Morning.

**Jan Rabenseifner:** Amen.

**Martin Spindler:** Morning. Are we complete or still waiting for someone?

**Tsz Yan Lam:** Sorry, can you say that again?

**Martin Spindler:** Uh, are we complete or how many are we missing?

**Tsz Yan Lam:** Ah, I think we are still missing a few colleagues, but I think we can actually start with the introduction. I think this is the first time meeting you Martin. Uh, nice to meet you. We also have a Martin in our team. Uh, so but I think the rest probably we already met last Friday,

**Martin Spindler:** Yes.

**Tsz Yan Lam:** right?

**Sven Klaassen:** Yes,

**Martin Spindler:** Yes.

**Sven Klaassen:** exactly.

**Martin Spindler:** Then maybe I introduce myself. So hello everyone. Uh I'm Martin. I'm professor of statistics data science at the University of Hamburg and co-founder of economic AI which is a spin-off of the university where the idea was bringing our research into practice.

### 00:03:04

**Martin Spindler:** So we do a lot of research on causal machine learning coal AI and I think this is really important for many real world applications and so the idea was uh trying to bring these methods into practice and supporting companies in applying advanced analytics in particular causal methods and what we're doing are mostly three things maybe probably you already know one is trainings like this here u which is direct transfer of knowledge u we also do consulting where we jointly with companies develop um models for challenging problems. And the last one is software development. So um our thing we are very proud of is the WML opensource package where we have been developing over the last years and we're also working on some add-ons to this package. So this is what we're mostly doing and today I'm looking forward uh to the day today with you. Um we split it up. I will start with a um a recap and um um use case session and then we have today some very interesting uh topics uh like difference indifference. Then we have a notebook session.

### 00:04:13

**Martin Spindler:** We also cover uh sensitivity analysis which is a quite new topic and at the end we also have enough time for Q&A uh recap uh and any other thoughts um we can uh we would like to discuss. Okay. Um maybe so let's start with a uh recap from uh last week. So uh last day um it started with an introduction to causal machine learning double machine learning. Then was a session on hyperparameter tuning and then um uh one session on treatment effective which from my point of view is really for applications in the real world but also of course in research very important um uh topic. Um maybe I start with an open question. Do you have any questions or points we uh we should discuss if

**Tsz Yan Lam:** Yeah, sorry. I'm trying to unmute myself.

**Martin Spindler:** yes

**Tsz Yan Lam:** Uh, one question that I have is so I think last week we talked about um how to use the package then we need to first find out the confinder. One thing that I'm interested in actually if you can anyone of you can share your experience is so typically when when we are only trying to learn association of the model then what we usually do is there are a lot of potential features that we can use and then we

### 00:05:47

**Martin Spindler:** H.

**Tsz Yan Lam:** will basically try to pass it through some machine learning models and

**Martin Spindler:** Mhm.

**Tsz Yan Lam:** then there are some technique that we can use for example to select features uh well I I think one easy way is look at the let's say the features important to say okay I only keep those that are important or there are some more sophisticated method that injecting some randomized version of it and then and then see whether the important or the signal is still stronger than those random one does it still apply in clausal machine learning or we need to be way more careful there in in in feature selection

**Martin Spindler:** Yeah, it's a very good question and the answer is needs to be very more careful because standard machine learning is really based on correlations and I mean see it's also very custom this kitchen sync approach throw in everything and the uh algorithms do the variable selection the problem is that all this is built on correlations I mean in the simple setting if you run a linear regression and you get the non-zero coefficient.

### 00:06:58

**Martin Spindler:** This only means that this variable is correlated with the outcome. So this means is had predictive power. This value helps me to predict the outcome. But this does not and this is for prediction perfectly fine. The problem comes when we want to intervene when we want to interchange when we want to set what is the optimal price level because then correlations are not good enough. Then we need to know what is the actual causal effect. um and and then all this causal inference is about how can we um uh solve this problem and I think it's a good starting question because then maybe we can also go through this process of causal inference uh how it works but but here the main point is we need to go beyond correlation so we um correlation is not sufficient I mean the simplest examples is or example I like you could regress um lung cancer uh and if someone uh wears a lighter him or her and you will get a strong positive coefficient. So wearing a lighter is highly correlated with lung cancer.

### 00:08:01

**Martin Spindler:** Uh and this is what you would get in a a regression and this is what you get in any machine learning methods. But the problem here is is this really causing it? Why is it important? Because when we want to uh improve the uh health of people then we need to know would forbidden lighters change something and then the answer would be no. And then um correlations are not enough and and this is I think an important or one way you can think about traditional machine learning is something passive you observe a pattern and transfer this in coal inference it's more active so you want to intervene you want to change something and if you want to do this you need to understand the mechanism and and this is a different exercise um and maybe there's something in between uh where you alluded to this is this big field of interpretable machine learning or interpretable AI and here you need to be careful because there was also a big hype in industry about this these methods are important but they tell you why do you predict something I mean in our simple AI model where we always if someone wears a lighter we predict lung cancer interpretable AI would tell us you predict for person uh lung cancer because he or she wears a lighter so you explain why you do predict something and here it's very simple but usually prediction problem can be very complex with thousand of variables And then they tell you what are some correlation patterns uh um makes them understandable.

### 00:09:26

**Martin Spindler:** But this does not mean mean if you change these various intervene then you get the desired outcome and this is what coal inference is about. Daniel you have a

**Daniel Jacob:** Yes. Um Martin,

**Martin Spindler:** question.

**Daniel Jacob:** can I maybe ask would it would you say it depends on the method that we're using? For example, if I'm using a linear regression, then uh maybe I need to be careful of adding um or deciding between colliders, confounders, mediators for example. But let's say we're using double machine learning where the idea is to do some of find some moment functions or do kind of this new human alterization and would you then say we would need to have only predictions for y and for the um propensity score and then to get the best predictions where we maybe can then build residuals on it doesn't matter because then we are still again in the prediction world or would you also say even in double machine learning even if we're interested in pred predictions. We need to be careful of variable selection.

### 00:10:23

**Martin Spindler:** Um I think the sadness is you still need to be careful. So it offers you a lot of freedom. Uh it gives you uh and we'll do this in the recap. uh will give you more freedom. You can have nonlinear relationships and so on which might be more realistic but you still have this underlying identifying assumption. You're fully right in double machine learning you have these two predictions where you send partial out and then you get invalid inference but one step before um you have still this identification part and for double machine so in the simplest linear regression setting double machine learning relies on the so-called unconfoundedness assumption. So this means all relevant confounders are included and this is still now again an identification assumption where double machineing PC does not help. The good thing is you might you might be in settings where you have many confounders. Yeah, you know them but um OS does not work because you have too many uh variables and then double machine learning helps you but double machine learning in the simplest there are of course many forms and today you'll see we can apply this to difference and difference but all these kind of models rely on some identif uhing assumptions.

### 00:11:35

**Martin Spindler:** This is the identification approach and and this is independent from the estimation approach. And here again this is something needs to think about. Do I observe the right um variables? Do I have all confounders and of course not including colliders as you have seen uh last time. So that we need the right conditioning set. The advantage of double machine learning is that if you have a very high dimensional confounders that we traditional estimation methods do not work um helps us um and and this is relation but maybe there are very good questions and very good discussion. So maybe let's step go one step back and the overall so if you have a problem in data science to solve I mean the standard procedures the first thing is do you have a prediction model and or do you have a coal inference problem I mean prediction models this is standard machine learning AI world it's almost a fixed pipeline from my point of view the most interesting problems are usually causal problems these are where we want to intervene want to change something want to optimize something and and the first step is always to recognize do we have a prediction problem, we have a causal problem and now if we identify the problem as a causal problem, I think the most important step is translating this problem into the language of um causal inference and this is really

### 00:13:00

**Martin Spindler:** uh often these problems are very hard but I think this is a good framework how to think problems in a principled way. What is your treatment? What is your outcome? In textbook, it always looks quite simple. In reality, when we come to use cases, you'll see it's often not so trivial. What is the treatment? How do you define it? What is the outcome? Is the outcome clicks in the next 24 hours, in the next 3 weeks, but is it more uh lifetime uh customer value, which is something long-term. So, what is your treatment? What is your outcome? This I think is what you so you need to translate your real world problem into this language of coal inference. And this helps you really to structure the problem. So this is I think the first uh step. And here what I also find an important step depends what you as a team uh uh do but I think important tool is really to for for the whole data science uh unit to adopt this language as a tool to think about problems.

### 00:13:59

**Martin Spindler:** so that you have really a unique language how uh to talk about problems because it's really a a formal apparatus for uh modeling this kind of problems. I think it's really important that or or a recommendation that you really if you have such problem start to think about uh these problems in these terms because this is really a well- definfined language because often you talk about coal effect it's very intuitive but here you have a formal language how you can reason about problems and and and how you can approach them and from my experience real world caused problems are always very hard uh because you have many mess but I think and and I would also say there's in real world problems not the right solution solution. I would not say you can say the price is 1.3. It's too complicated. But with this um methodology or um uh language, you can really think about this problems and then find good solutions which come as close as possible to an uh true realistic solution uh where you finally can base on decisions which make sense because this is why are we doing coal inference?

### 00:15:04

**Martin Spindler:** because the inference is an intermediate step because the ultimate goal are better decision. So how should you set the optimal price to um uh maximize profit? So this is what we ultimate after but but I think this is the first step is really using this language to translate your problem uh into this language and now and so this is it uh translation step and then the next step is the modeling part or and the estimation part and and and here it's um before the estimation comes the identification part and this is a fundamental question given your data is it costly effect identified at all. And now we have here two ways. One way is we could collect our data on our own and do an AB test. And I mean AB test now in in tech industry is a booming field because it's so cheap to set up and there's been a lot of development and and but AB test is one classical word how to uh estimate or identify cost effects because in this setting by definition your causal effect is identified you have seen this last time.

### 00:16:13

**Martin Spindler:** If you have an IB test, you can simply compare the mean between two groups and and this is how it's identified. Here two things uh of course also in at least from my experience also in real world experiments many things can go wrong. So here one needs to be very careful how to set up things how to do the randomization but in principle AP tests also gold standard to estimate coal effects and here also it's an old topic in principle uh in uh AP test you need to compare two means but of course there's also now a lot of innovation where people use double machine learning to evaluate such experiments to find hogenous uh treatment effects to find uh uh much uh richer uh patterns. So this is um also a lot of stuff is going on in the classical AB test world uh because many problems arise. Uh I mean one is this heterogeneity which is an important topic because this is a key uh for personalized uh policies uh for targeted marketing uh these are nothing else in heterogeneous treatment effects.

### 00:17:22

**Martin Spindler:** So this is there's some new development um uh going on in this classical AP setting but this is now a booming field and um all online tech app companies do this because it's cheap to set up. So this is the one in our toolbox how we can learn causal effects is one is a a world of uh AP tests. Uh J, you have a

**Chieri Naito:** Yes, sorry I didn't want to interrupt.

**Martin Spindler:** question?

**Chieri Naito:** Maybe you should because I had a question on the heterogenei um as effect. Um I think uh you know adding to Daniel's point I was also thinking you know okay first stage we will choose the features very carefully you know by you know uh mapping everything and you know we would removed of course like collider and mediator that sort of thing and we will be careful about like certain instrument variable whatever but after that um after that feature selection okay there is first stage and then double machine learning there's second stage and then if you want to uh um you know uh choose certain features for the heterogeneity uh we still need to select some features from uh subset of features from it and there I think what Daniel uh also meant is uh there because selection feature

### 00:18:35

**Martin Spindler:** Mhm.

**Chieri Naito:** selection is already done based on the causal graph uh you know everything should matters at least you

**Martin Spindler:** Mhm.

**Chieri Naito:** know it's not pure um correlation but there we think that there's a causality Uh but then we need to choose like two or three features and there like for example uh using um like a generalized uh uh um um u random force like for example like this model is the split is made in a way to maximize the heterogeneity uh right

**Martin Spindler:** Huh?

**Chieri Naito:** so we can rely on you know like this feature importance that's what I thought and and in And in the end um you know

**Martin Spindler:** Huh?

**Chieri Naito:** if the sensitivity analysis that that's what we all care about right uh if we have you know that sort of validation data offline um then as long as this metrics looks good um um I don't know this sort of uh feature selection is acceptable like seems seems to me like that but uh yeah if you mentioned about this you know heterogenity thing is booming. So I would like to know more about it.

### 00:19:57

**Martin Spindler:** Mhm. Mhm. No, no, it's a very good point. So, and and you raised several points so I took some notes. So, because you said these two steps and I think it's important the first step is what we still this is the identification part. So under which conditions can you is your cause effect identified and now we had AB tests where it's identified by design u and of course in this AB test you can also check for hetrogenous treatment effects and maybe I come to this uh later so this are the AP tests and then you have the other big cause these are observational data so all data which do not come from an AP test observational data and now the question is under which conditions can you learn causal effects from observation data and we have seen it's not given so you can have observational data want to estimate and cause effect where where it's not identified where given the data you cannot answer the question you want to answer I mean if I give you information about um wearing a lighter and lung cancer status and there's some variable missing the smoking status you would need and with this limited information the cause effect is not identified and now the first thing if you have observational data is to think about under which condition is the causal effect identified and here the step has nothing to do with machine learning AI this comes later in the estimation part and now we have

### 00:21:22

**Martin Spindler:** a certain toolbox I mean the first uh thing standard assumption is the so-al unconfoundedness assumption can you check or be are you assured that all confounding variables are contained in the data set if yes you can so somehow rebuild the assignment mechanism you can control and you can make the groups comparable and you're fine. So and we have seen as you said um unconfoundedness assumption needs not all confounded needs all back needs to be closed no collider so this a little bit the technique behind but this is unconfoundedness assumption do I observe all relevant confounders and this is usually an untestable hypothesis because um you need to take this assumption so this is something you need to discuss but later today we have also a session on sensitivity analysis it's quite new field but I think this is really very important Because this can help you to validate this assumption because uh in a lot of practice people work with this unconfoundedness assumption and then there are discussions have we not omitted here in variable which would invalidate our results and with sensitivity analysis you can make this analysis stronger.

### 00:22:31

**Martin Spindler:** So this is say unconfoundedness assumption. This is one tool how we or set of assumptions how we can learn causal effects. The problem is there's um there are different kind of uh tools and all come with different kind of assumptions and this you need to validate. I mean observing oil confounders is a very strong assumption and I mean in some situations um it it would not hold. So you have unobserved confounding. And now the question if you have an unobserved confounder can you still identify as a causal effect? And here's the answer again is yes, but additional assumptions need to hold. So no free lunch. If you have unobserved confounder, you still might learn um causal effects, but you need additional assumptions. And since there are classes you have, you already mentioned instrumental variables. Uh to uh today we cover difference and difference. This is a very widely used uh experimental design. you can unobserve confounding and related to difference and difference are synthetic control which is also now I see a lot of applications in industry because it overcomes the problems of uh difference and difference then we have panel data settings panel data where you have observed individuals over time are also important source where you can uh control for unobserved confounding uh and and then also you have regression discontinuity design which user special setting.

### 00:23:59

**Martin Spindler:** So these are tools so to speak you could leverage in in when you have unobserved confounding but again they come with additional assumptions and this is now when you have now your problem you need to think about what assumptions to hold for my problem. So what is an realistic assumptions uh which might hold. So this is the identification part. This probably is the most important part. Now comes the estimation part because now you want to estimate your causal effect. For example, you say unconfoundedness assumption is um uh holds. Uh I'm convinced we have all relevant confounders collected and now you want to estimate your causal effect. And now the problem might be um you in a high dimensional setting where the effect of confounders might be nonlinear. You might have too many uh confounders and then double machine learning is so to speak a estimation tool. And now you see again for double machine learning you have the identification part you have the estimation part uh which is separate and double machine learning is in the first line a tool for inference on target parameters in high dimensional settings and if additional assumptions holds it gets interpretation as a causal effect but this is some two separated things and now what's now going on is that um this methods difference indifference regression are all combined with machine learning methods so that they allow for richer control of variables allow for more realistic settings because you can have

### 00:25:27

**Martin Spindler:** many coariat so the effect of the confounders can be highly nonlinear complex and you can capture with this Daniel you have a

**Daniel Jacob:** Yes, just to um follow up on on what Cherry was also kind of linking confounding with effective

**Martin Spindler:** question

**Daniel Jacob:** generity. Um I think correct me if I'm wrong, but is it um just because a variable is a confounder does not necessarily mean that it is also kind of contributing to effect generity, right? So you could have just one treatment effect for all but still have a lot of confounding variables.

**Martin Spindler:** Yes.

**Daniel Jacob:** So I think variable selection in these two stages is also independent

**Martin Spindler:** Yes.

**Daniel Jacob:** right.

**Martin Spindler:** Yes. And and and this is now exactly because I now wanted to come back to hogenating Kate because up to now I explained the overall picture. So um when is a cause effect identified? How to uh have these different kind of causes and how to select them and now um there are different kind of causal effects. I mean oil started with the average shipment effect but this is by far the most uninteresting effect.

### 00:26:31

**Martin Spindler:** So the average shipment effect tells us what is the effect on an intervention on average. I mean in some situations is important but usually we observe a lot of hogenity. I mean classical example in medicine uh the same dosage of a drug has a different effect for men and women for children grown-ups and I mean in marketing um the effect of an promotion might be really very different depending on age and so on. So this means the effect is different in subgroups and this is what effect heterogeneity is about and last time we you learned the gate the group average treatment effect that is variable is um categorical one or the kate that's a continuous variable in principle could have also uh combinations and uh here it's important that this hogenity so heterogeneity tells us how does the uh treatment effect vary according to coariats and this coariantss need not to be any causal and therefore in bioatistics they are often called effect modifier because they modify the effect but it's far away from coales there could be all complex relationships but now coming back to a practical point of view usually you know or have some on the one hand machine learning can help you to detect heterogeneity to identify the subgroups but often uh you also um have already guesses.

### 00:27:59

**Martin Spindler:** I mean you might think okay my marketing uh campaign might depend on the age of the people of gender of rule or area but you could also do variable selection to find out in what dimension do you have heterogenity um and why is this important because if we know uh how uh subgroups react differently we can then develop targeted policies. If you know for example for this group uh the um um marketing campaign has the largest effect uh you can of course um target those and for those negative you won't target at all or often uh this I also wanted to say um this causal models is usually the first step. So if you have estimated the heterogeneity the second step or this is then used as an input in an optimization model because for example in marketing you might test an overall budget and then you might know how different subgroups react and then uh it's an optimization problem to decide whom uh to target for example um and and this is nowadays also uh in research but also in uh industry a booming field so that you and it's also called policy learning.

### 00:29:07

**Martin Spindler:** how to find for individuals the best policy uh to treat them and one way is finding heat originality uh and then uh doing this um and now um coming back Jerry to your question of course you can have causal forest where the splits is done in a datadriven way where you select what are the subgroups where you have heterogeneity or there also other approaches you can also have WML style uh heterogeneity um and there are different kind of learners to find these patterns always pros and cons but this is again the estimation part. The conceptual part is here that your effect might vary according to variables and and and you would like to estimate this but this variables need not be causal. So this is pure uh correlation based. So this means in this subgroup uh according to age um there's a different effect but how the mechanism is how it works this is um again would be causal modeling uh but but this here is um hetroenity in which dimension does it vary

**Sven Klaassen:** and may maybe just just a very short addition to that.

### 00:30:15

**Sven Klaassen:** Um so so you said specifically also for for um causal forest which tries to to maximize sort of the hetrogenity in the splits. So, so it maximizes the hetrogenity in the splits with respect to the features X or confounders you're putting in, right? But if you want to have then effect hogenity with respect to something else, you you you would run the same thing that you are doing in in in WML for the Kate some sort of best linear um projection. So So I can for example there there's a link on the the here in the I post in the chat on the documentation. So it's exactly the same thing what we've seen um yesterday at the end um at the last session. So so essentially trying to project in our case that's part of the score in the their case that's sort of the the Kate at the the lowest level which is nearly identical just using different machine learning models for predictions. But in principle you can then try to project it on anything else. So, so doesn't need to be specifically something which you're using as confounders.

### 00:31:22

**Sven Klaassen:** Could be something else like Martin said it it's it's just like this how the effect modifies with with with these features. So there it's also called then a because it's it's different from X, right? So so sorry for the interruption.

**Chieri Naito:** Thank

**Sven Klaassen:** I

**Martin Spindler:** No thanks and thanks for stepping in. So uh this I would say was so as a big picture. So how uh the course workflow is and what the steps you need to take and how these things relate. But this I think it's the most important thing to understand is first translation into this language treatment um potential outcomes then doing the modeling uh and then the identification part. So um how is my causal effect identified? Can I learn this from the data? And and if this you decided on a model, the next step is since then the estimation part and as I said if you're in a high dimensional complex setting uh standard methods fail and here's this with double machine learning kicks in so far. Any questions on this big picture how things are related?

### 00:32:28

**Martin Spindler:** If not then maybe I would now go a brief uh recap on double machine learning only. Uh I mean I think Daniel you perfectly already recaped this that we have um uh this prediction problems from the outcome treatment uh and partial out effects but maybe have a brief look at again a short reminder why this is necessary what drives double machine learning and then maybe I can also uh present some use cases uh to give you some flavor how this is applied. So maybe I briefly share Can you see my screen? Perfect. Thank you. So here uh let's start with for this question. Can you see my screen? I've never got so many thumb sums up. So this is great. Most of the time I was begging for feedback, but Uh okay so uh recap I I mean this I skipped this is I wanted to cover informally and I hope this big picture this is really uh very important so this is and now let's assume so you we translated our problem in the course language um we now decided okay unconfoundedness holds so and now here we have the partially regression model so y is our outcome D is our treatment variable and X is or confounders.

### 00:34:01

**Martin Spindler:** And the effect of the confounders could be highly non apologies I'm talking too fast. So um so so this is a partial linear regression model which has an somehow additive structure of the confounder and treatment effect but the effect of the confounders can be highly complex nonlinear function. And now if unconfoundedness holds theta not has the interpretation of an causal parameter. this is our policy variable or target parameter. Uh this could for example is often could be also price elasticity. If you regress demand on low prices uh then s not is for example a price elasticity and now so this is a cost identification part and now we have an estimation part because now we want to estimate the not but we are now might be in a high dimensional setting where OS does not work because we have too many uh features in the model or less does not work and now the question is how can we estimate a saut and now a knife approach would be okay let's use machine learning to estimate here's the nuance part because machine learning are good in learning complex functions.

### 00:35:14

**Martin Spindler:** So we use machine learning to learn this one plug it in and then regress y on d plus this plugin or subtract it from y and and this is a knife approach which sounds reasonable but the problem is inference breaks down. Um so sa not uh our estimator for sa not in this procedure will not be normally distributed will have a bias. So this means if we form confidence intervals they will not be valid. If we base decisions on this confidence intervals on average we'll lose money because we'll take on average biased wrong decisions. And now the question is how can we estimate siton not reliable? And here's the answer is double machine learning. Um and and here an interesting part is because machine learning is developed to predict uh y and in high dimensional settings we have overfitting. So we need to have some regularization bias uh to avoid overfitting for prediction. This is perfectly fine. But if we want to learn coefficients this is a challenge because in approach machine learning methods if I use lasso have a look at the lasso coefficients they are biased um uh distribution unknown of this uh estimates.

### 00:36:26

**Martin Spindler:** And now here double machine learning helps us out. And and the name double machine learning says this. We need to apply machine learning twice. And therefore here we introduce this auxiliary regression or we model the confounding. And now the idea is we run two regressions. We regress D on X and Y on X to estimate the so-called nuisance part. So we estimate G not of X M and M not of X. And now what we're doing is we're partialing out we're taking out the effect of X from D and Y. So this means we subtract M hat and G head from Y and D and get the residuals. So we use machine learning methods to take out the effect of X from Y, take out the effect of X from D and then so we take out the effect of X from D and Y with modern machine learning methods. And now we regress the residuals on each others. And now if we do this we get an estimator for SA which has nice properties which is normally distributed centered around the true value and this is double machine learning.

### 00:37:30

**Martin Spindler:** It is a method an algorithm which allows us to get with machine learning methods valid inference for target parameters. So this is a nutshell what double machine learning uh is about. And now you could answer okay and here I I really do not go into detail but for those of you who maybe have a background in echometrics or statistics. So we have these two approaches this knife approach which gives us uh biased estimates and the double machine learning approach and why does this one approach work and the other not the key insight is that pro both approaches rely on different kind of moment conditions. So this I do not go into detail it's technical but moment conditions are this methods you use to estimate your parameters and the moment condition um the knife approach looks works on is the standard OS moment condition the double machine learning approach implicitly creates a different moment condition which has a special property which is called nimman autoonality so this means nimonality means we have we estimate this machine learning method nuisance parame parameters. Um, and if you use an and and this new so we use machine learning methods to estimate nuisance parameters and plug them in and this plugin might have an first order effect on our target parameters and the nimon orgonal moment condition secures that this estimation errors in the nuance pot

### 00:38:56

**Martin Spindler:** have no first order effect on our target parameter. Um, this is a nutshell what this nimonality is about. But this is if you apply this stuff not really important. But now people are currently searching how this nimonal form for different kind of models looks like because if you know the how these forms looks like you can estimate this model with machine learning methods and get valid inference. So this is as a motivation uh why this is uh done. Uh and maybe here if you have questions I'm happy to dive into but otherwise I will maybe um um stick to the high level parts um and maybe here's the last comment. So now we consider double machine learning for the most simple setting for the partial linear regression model. And now if you apply double machine learning of course you need to take care of some things. One thing was mentioned you need to do cross fitting because if you use machine learning methods to estimate the nuisance part you still could do overfitting. And the idea is you split the data in some parts you use uh in in let's say five parts you use some parts to estimate use parts and the other ones for the inference part.

### 00:40:07

**Martin Spindler:** This is needed that you don't overfit with random forest or other methods. So this is uh crossfiting. Another thing or frequently asked question is I have a lot of freedom because you can choose uh the learner for the nuisance part. You could use a random forest, you could use an elaso. Which one should you use? And people found out that with different kind of learner you might get different estimates for a target parameter. And here's the rule of thumb is that you should always use this um um method which gives you the smallest prediction error for the nuisance part. So you have a choice of learners for the nuisance part and you should take this one which somehow has the best predictive performance. you still can have bad luck. But this is uh some guidance how to uh choose this. And I think also on the web page for WML, we have also some guidance because now with AutoML or OP uh optotuning um you can uh automate this a little bit um and um um get more uh robustness.

### 00:41:14

**Martin Spindler:** But this was some something people were struggling with because with different learners you might get different results. But now um I think Swen uh sometime we released this uh Swen implemented this was optotuner where you uh could do some optimized hyperparameter tuning. Um any questions on uh double machining? Annie, you have a question.

**Ani Pole:** Yes, just a clarifying question. So you mentioned Neon's um orthogonality, but like I mean when I'm looking at the equation, does it mean that basically the treatment is independent of um the residual of uh what we're trying to predict with the nuisance model or I mean how would you interpret this in in a

**Martin Spindler:** Um yeah real world example

**Ani Pole:** real world example?

**Martin Spindler:** is difficult because it's a pure technical thing. So it has nothing to do with your variables. It's a technical condition and it means so a moment condition is something which identifies your parameter. So a moment condition depends on the data. It depends on the target parameter and depends on the nuisance parameters and and and this identifies so to speak your true parameters.

### 00:42:22

**Martin Spindler:** So the expected value of the moment condition at the two parameters is equal to zero. So this is some kind of identifying assumption. And now nimonogonality means if you take the partial derivative of this moment condition with regard to the nuance parameters and evaluate this at the true parameter values it's equal to zero. And this has an very in intuitive explanation because this means if you usually we don't know what are the true parameters we do not know the true target parameters. Therefore we do the estimation but um at the true parameter values for the targeted nuisance part this means if we are at the right parameters if you do a small change peration of the nuance part it has no first order effect on the target parameter. So this needs non autoonality and the point is estimation of the nuisance part with machine learning methods introduces some errors because uh lassus makes some variable selection mistakes. So this means if you use machine learning methods to estimate the nuisance parts we create some noise some perturbation in the nuisance part and now nonogonality means if I plug in this estimate of the nuisance part in my moment condition and solve for the target parameter it has no first order effect.

### 00:43:38

**Martin Spindler:** it does not introduce a bias. The knife method, so the standard OS moment condition does not have this um condition and this means if we estimate the nuisance part this machine learning method, it fully uh hits us into the target parameter. uh because this error we make directly translates into error of the target parameter and this nonality means we have some uh security uh safeguard and and this is the problem that lasso they're very good for prediction but they always make some small selection errors and the problem is that if you use lasso to select the co-founders in the main equation um the lasso will always pick this variables which are highly correlated with the outcome but it might be you might have an confounder which is not important to predict why but it's highly correlated with D and if lasso misses such an variable it creates an omitted variable bias and non autoonality is a safeguard so that set um this model selection errors do not hurt you for the target parameter it's a very technical um condition so it's nothing one can illustrate in an um uh example but this is only as I said it's a technical point if you want to apply this stuff it's not important at all I only wanted to give you some intuition and and double machine learning is really centered about this autoon moment condition.

### 00:45:01

**Martin Spindler:** If for a model you have this autoonal moment condition we can easily incorporate this in double machine learning. So um because then you have this cross fitting all the steps can then be automatized and modularized. Um I hope this clears the point but this is really sub technical point but I hope you got the intuition that this is really for estimations the key thing that we our target is a estimation for the target parameters in some sense immune to uh errors we make it a nuisance pot and this is machine learning methods always do come any other

**Ani Pole:** Okay, thank

**Martin Spindler:** questions yes uh

**Daniel Jacob:** Yes, a short followup.

**Martin Spindler:** Continue.

**Daniel Jacob:** Um, so does this mean um let's say I have two machine learning models. Let's say I'm using a large GBM model or some treebased model and also neural network. So I know that astoically they they are all fine with respect to the nuisance functions. But then so how would kind of the prediction accuracy of these two models play into into this?

### 00:46:05

**Daniel Jacob:** Um,

**Martin Spindler:** Uh uh

**Daniel Jacob:** of course I want to choose the one with with a higher prediction, but but does it really matter?

**Martin Spindler:** it's

**Daniel Jacob:** I mean, like how does this translate into kind of the um the the new um moment condition?

**Martin Spindler:** yeah this is a very good point. So asmtotically it does not matter because if you have enough data al should give you the same predictions and and should not make a big difference that this here is really a small sample problem because you have limited data and of course also for prediction lasso random forest for prediction problem if you have small data might behave differently. I mean lasso boosting they all should behave similarly asymtotically should generate have the same rate of convergence. So asymmetto should make not make a difference but you see and what we're doing here we leverage machine learning for predictions because what we really after is predicting y and predicting d and this should be as good as possible but now what we discuss here it's a small sample problem asmtotically you don't have any problem at all but you know or already have experience on your own that even if you have a prediction a small data set you use lasso you use um uh um this different methods which give you different results and in predict It's clear you always use this method which out of sample has the smallest prediction error.

### 00:47:21

**Martin Spindler:** So this is usually how you select among uh learners and here it's recommended doing the same. Here our downstream task is estimating a costal parameters on the way we have this um prediction problem and now we might have different learners and here again recommendation is use this ones which have predicts the nuance parts best out of sample but this is really uh a small sample thing and and it's not um there are some approaches thinking about this but this is really more an empirically small sample

**Sven Klaassen:** and and and just very shortly for for this small sample the reason why it's a small sample problem like you said Martin is it's it's the first order effect is zero right so so but if you think of tailaylor expansions and things like this there are second order effects third order effects things like this. So better predictions are still then better overall for for your your estimation like but like Martin Vin said then asmtotically all these things vanish and and so everything is there the same but but in in your in standard problems you you then essentially see something like the second order effects of

### 00:48:39

**Daniel Jacob:** for elaborating

**Martin Spindler:** Okay, any other questions? If not then maybe we have u uh most a little bit more than 20 minutes over then maybe I would present some use cases so that you maybe get some inspiration how this stuff could apply and of course we could also discuss if you have some ideas um um I think in the precourse you mentioned um I mean problems are everywhere but maybe have some specific and also at the end in the closing uh we could uh uh come back um later to this uh again So, one second. Uh, I think because I'm uh Martin,

**Martin Bierey:** Yeah,

**Martin Spindler:** you have a question.

**Martin Bierey:** maybe just for the use cases. So one thing that could be also interesting for us is so I think when we speak in the workshop about heterogeneous treatment effects we mostly think of the cross-section. So treatment effects being differently for different groups of customers or similar uh I think in our case the time dimension is also very important. So if we think of different versions of dynamic pricing, it will matter a lot um what the optimal price level is in what time period you are.

### 00:49:56

**Martin Bierey:** So I'm not sure in the use case we go through if there's anything where the time dimension plays an important role. Um that would

**Martin Spindler:** Um and I think there's no example for this but of course this is we can discuss so because you're fully right you have this time dis mention I mean there's one use case where it shows up a little bit but but maybe this is something also for the uh it's very important uh point uh I took a note and then along the way we can discuss this and that's the closing We also have some time in the afternoon for exactly discussing points like this. Okay. Uh hope you can see I now uh switch to PDF file use cases. Uh can you see? Okay. Perfect. Uh so uh as I said there is two words of experimentation and observational data and I as I said this is only for input for brain uh uh storming what how these methods are applied but of course there are plenty of methods and each company has different pain points or different challenges.

### 00:51:12

**Martin Spindler:** Um here I wanted to start with the word of AP testing to show that double machine learning or um these methods can help also in the classical AP test world. So what here was the problem? Um here I brought with me two AB tests which are quite similar. So the first one was about website optimization. So this was for a car manufacturer who have a market um uh um sorry so they have uh in a market um uh problem where stock cars are used a lot. So in in Germany usually if you buy a car a new car it's produced on demand but in other countries you have them on stock and people go to the website and and now the question was how should you do the ordering or or how should you design the starting page because for example if people look out for a new car and the expensive ones are at the beginning uh they might leave because think it's too expensive. Uh so the question is how should you design and how should you present uh the cars so that you can engage customers so that they click stay on the website and finally um uh of course ideally buy one and here of course it might be um uh important to have a dynamic or or uh uh personalized policy because um for some users it might be the best showing the expensive cost first for some maybe a different strategy.

### 00:52:45

**Martin Spindler:** Now the question here was how to find out how to personalize the website and the idea was it's a causal problem. Um and then of course first translating in the coal language then here an AP test uh was run uh with different kind of versions and then on top of this in the analysis it was uh tried to identify different subgroups to find for each subgroup as the best one and here finding for example was day of the time is important and not surprisingly device. So if someone uses an Apple device, uh it might uh be a heterogeneous effect compared to other devices. So this was here's the idea. But you have a

**Tsz Yan Lam:** Yeah, Martin, it's not really a question.

**Martin Spindler:** question.

**Tsz Yan Lam:** So, I think the presentation right now you have uh this minimized wheel that are that are showing that are blocking the whole slide

**Martin Spindler:** Okay. Uh sorry,

**Tsz Yan Lam:** actually.

**Martin Spindler:** is it better now?

**Tsz Yan Lam:** Thank you. Yes, thank

**Martin Spindler:** Okay.

### 00:53:40

**Martin Spindler:** Sorry. because in zoom sometimes the fewer do not see this box in in it's always different from each uh program. So apologies that it was such big thing. Um so so here the idea was doing an IP test and then finding heterogeneous subgroups and then to uh do some personalization of the uh web page. Um and of course here are different uh KPIs because buy is a very rare event but it was really uh do they stay on the website? Um do they click on the cost and so different KPIs one can um uh discuss but of course one can shows that this really help to personalization help to improve the time spent but also uh page views. Uh here again another example also AP test um car sharing. So what is the background setting? So uh it's a big car manufacturer and and they also have some kind of services and this is a service probably Germans would never rent out their car but in Eastern Europe it's popular that if you have a car you can they have a digital platform a service where you can register your car and if you go two weeks on vacation uh you can uh rent out your car to other people.

### 00:55:02

**Martin Spindler:** they pay uh for this period uh the platform gets some fee. Uh this is the idea and now it's the following problem. It cost a lot of marketing expensive to bring people to register to this uh website for the service. Uh but then they only did it once uh and they never came back. And now the question is how can you activate users uh to come back? Uh and this is of course a causal problem. we have an intervention uh and we would like to know what is the effect of a certain intervention on outcome that's a comeback and um what is intervention the idea was sending out wishes because uh you get an email if you use our con this service next time you get a discount of this and this and now the problem uh is that what is the optimal voucher size if you uh send out a too large uh coupon voucher you might lose money if it's too low. People might not activate it. And you could think about that um the the uh voucher size might depend on characteristics.

### 00:56:11

**Martin Spindler:** So there might be heterogeneity uh men women depending on the age might react differently and this was the purpose finding out um identifying subgroups which react differently to find um the optimal um uh strategy uh uh how to target uh customers. Uh I skipped this but here again the idea was um and the first question is is if you have a cause a problem should you use past data or should you do an AB test here in this example they um were happy to do an AB test where uh different via sizes were sent out and then uh these methods were used to identify uh subgroups and here an interesting finding was that there's really hogenity and drivers um all variables which drive originality of for example gender. We have seen men and women react differently. There was also a difference uh in uh rural areas or cities which is also not surprising because city you have more uh competition. Um rural area if you need a car you might have less options. Therefore also with a smaller you already are activated and H and this was really then developing strategies um then where you um uh target um customers according to this uh segmentation.

### 00:57:41

**Martin Spindler:** And here again uh one could really prove uh that with this um measures one could really improve uh improve the engagement with the website and bringing back customers because as I said it's really a lot of marketing spend to bring them to register once and then it's important really to uh activate them again otherwise it's somehow um sunk costs for getting them once here typical examples As I said, AB testing is now extremely booming. It's used a lot for improved customer journey, how you should design uh things uh like website layout optimization, uh personalized marketing, it's extremely used a lot and of course for pricing in general. Pricing experiments for pricing is um a little bit tricky. There's often in the classical industry some uh doubts on this, but in the digitalized world if it's small amounts um you can really try this out. But it's also done now for um um to find out the willingness to pay also for more complex products. This was um AB testing u so far. Any questions? So these are typical examples.

### 00:59:03

**Martin Spindler:** As I said, AB testing is widely used in tech industry and platforms. what what's new is a little bit um combining this machine learning methods to uh detect heterogeneous subgroups and also doing um say inference uh correct so to speak because if you try too many things you um it's important to do the inference correctly and you have a

**Tsz Yan Lam:** Yeah. Yeah. Maybe maybe the last one that you already mentioned yo you're talking about. So of course I understand the concept of AB testing but I also uh uh have read that this is also dangerous that you keep well you collect your data in AB testing and keep sliding until you find something but but because you at the end find something if you

**Martin Spindler:** Mhm.

**Tsz Yan Lam:** slide if you are diligent enough what is your comment on on

**Martin Spindler:** Yes, this is a very important point because and now as um AB testing is used on such a large scale, you have this problem. you decided you might uh because if you do thousands of experiments you will find something spurious and this is what we see because um companies like MS Netflix they do really AP testing on a large scale so they have internal platforms where even an analyst can start the AP tests and now if you think about that you do

### 01:00:19

**Martin Spindler:** hundreds of AP tests uh in a in a months this really um adds up and and and and there has been some criticism that um that you have this burious finding things because if you do thousands of experiments you find something uh and or paper I think it was recently one or two year ago in management science maybe I can u look out for this where say uh exactly discuss this point uh and then of course um um you can also do uh improvements on this so there are statistical tools um but but but you need to be careful as you said if you do this on a very large scale Um uh this is a challenge and and then also uh another challenge is in the past of course when it was difficult to do you did it for big problems but now these tech companies do it on a large scale for small incremental improvements. So uh and then if you only uh are after the small then it's even more tricky to find what is noise what the signal and this has led to some problems because they overdid it with really large scale experiments and then um you might go in the wrong directions but I would say a bit is a really still powerful tool but as you said you need to be careful uh when you do it too often and um maybe question to you do how do Do you do a B test on which scale?

### 01:01:46

**Martin Spindler:** Um

**Martin Bierey:** I would say on a quite large scale and in all kind of areas. So the probably the most active ones being the marketing teams. Um but then also we do it in pricing.

**Martin Spindler:** Mhm.

**Martin Bierey:** We do it like in a lot of places and also usually when we bring machine learning models they get a bet tested first.

**Martin Spindler:** Mhm. Okay. S you already use it a lot and are used to it. So um and as I said AB tests are often considered as a gold standard of causal inference uh because they allow a clean estimation but also some problems come with them. And I think the strength of machine learning is really this finding hogenity but one needs to be careful if you do this on a too large scale. there are some pitfalls involved and I mean also setting up clear experiment is al always not so simple and then often the question is whom have you actually targeted um and then this relates and also the question what costly effect are actually estimating because often think about the average treatment effect but let's assume you do something only on your customers then you have the word of not customers and there you see you often do something on a very specific subgroups and then you need to be careful what are actually estimating at all

### 01:03:02

**Martin Spindler:** even with AP tests. Uh Daniel,

**Daniel Jacob:** Yes,

**Martin Spindler:** you have a question.

**Daniel Jacob:** I was also just kind of wondering regarding um doing a lot of AB tests um and then as you said maybe of the standard would be at some point you stop with the AB test and then you evaluate it and then of course if if you run a lot of AB test you find some serious um correlations there would you then maybe recommend uh one way could be to I don't know apply some multi-mbbended for example and and at some point of time shift towards a a more promising AB test, but then just let it run longer so that you can kind of eliminate the so that it just does not look at once um at the results um but for a longer time and see if it really if this effect really kind of um is stable or or how would you kind of then recommend if you find something um to kind of evaluate if this was spurious or um or not?

**Martin Spindler:** Mhm. Yeah, this is a very good point and we see also some uh innovations in this field which try exactly work on this uh because in the past when you do an experiment classically thing you set up for certain time frame but now things get more and more adaptive.

### 01:04:14

**Martin Spindler:** So this means you let run different alternatives and then if you see this is significant then you stop um and and and discard maybe this one which is not and and then focus on the significant. So there's now more adaptivity that you earlier decide uh what makes sense and what does not say makes it involve that you don't need to wait too long or invest two things and of course as you said bandit is now a topic which is a lot of use where you have several options and then you experiment in parallel which it gives you some adaptivity because uh classical is something very static you define for two weeks we run this option but now since people are more impatient so uh you you do really more adaptive things. Um and and bandits is has been in the last years of course hot topic exactly in this uh online experimentation world because it uh helps a little bit to overcome the challenges and of course validation is also important because if you do larger changes then of course you can also validate this with an AB test and we'll come also to this what I'm twofolded on this but often if you do a learn cause effect from observational data and it means a problem in general general causal inferences that we do not know what is the ground truth and then what often do people use observational data to estimate an effect implement something and then they might do an AP test to validate if it's uh actually what we want to uh wanted to see or what we expected so this is often

### 01:05:47

**Martin Spindler:** combination doing observational data do something and then maybe evaluation with an AP test but this is of course expensive and also has some pitfalls but this is Um I see any other questions on this topic. Uh if not then maybe I share back and come briefly to uh but as I said at the end we have also uh still time. So um to dive deeper into this um let me share this. So now I have some use cases um for learning from observational data. So we started with a test now we come to observational data. Here I brought one example. This is typical estimation of price elasticities. Um so here is an example from a retailer but this is a general principle that price elasticity we want to estimate. So if you regress log demand log quantities on log prices the corresponding coefficient is uh elasticity. But here of course it gets tricky is the identification part because you might have a lot of confounders because I mean there are many variables which effect the price like quality but also the demand and here the question is of course what are the right confounders or or or do you observe all relevant confounders or what identification um strategy you can use.

### 01:07:21

**Martin Spindler:** So here often for elasticities pendal data are leveraged where we observe one product I over a certain time. Um of course we need some also contain some price changes and then we might increase a high dimension set of um control variables which describes the product which describes the competitor products and then we in a high dimensional setting. The first thing is identification part and um then we might come up with a panel data model and want to estimate this but now we might be in a high dimensional setting and then we can use double machine learning to estimate the price elasticity and then of course in the next step one can use this uh for pricing. Um and here in this example this is based on an uh working paper or project uh a working paper came out of this but this was a project Victor Chennosukov has done um with an retailer in UK and the interesting thing is that here they really after estimating the elasticities from observational data they did then an AP test for certain products to validate the results.

### 01:08:29

**Martin Spindler:** Um here another project um dynamic pricing um and this here if you're interested we also have uh articles on describing uh this project. Um here's the idea was how to optimize the pricing for ride sharing. I mean everyone of you probably used right sharing. It's typical digital service where you enter your starting point uh end point and then you uh and starting point and then you get um price uh shown. Uh the problem is that their pricing scheme at the beginning was very simple. It was proportional to the distance and then they um asked for developing a dynamic pricing system where the price should depend on more factors. Um and then um the task here was really building an pricing model and here again it's first important to understand it's a causal problem and then one can think you could do AP testing but they did not want to do the AP testing in several reasons. So we had to use observational data and then uh build an um customer choice model um uh to model how say a so-called structural model to model how customers do their choices and then estimate structural parameters from the data.

### 01:09:41

**Martin Spindler:** So what is the willingness to pay under certain conditions? So heterogeneous treatment effects and then based on this proposed pricing schemes um which somehow maximize uh certain KPIs and the demand then really became uh dependent on many factors like weather conditions, day of the uh week day, day of time of the day but also from the starting and end point. So this is I like this plot here because this shows how the price depends on the start and ending point. So this is a Chinese city and but the interesting part is in a datadriven way it was determined that here in the red areas you pay higher prices and uh these are really uh the business uh and financial district of the city. And you know business travelers if they need to go to the airport station they are less price elast uh price sensitive and pay higher prices. and and this was really a datadriven way to figure out what are the drivers uh for um the willingness to pay and then incorporate this uh into the pricing scheme.

### 01:10:44

**Martin Spindler:** Uh another example uh I I I like this a lot. So on the one hand of course we have worked a lot on this but uh it makes a good point between prediction and causal inference because many companies they do financial forecasting so that you want to forecast how many products uh or services you sell next quarter or year ahead. This is a typical prediction task and this is usually data scientists develop prediction models. But now if you have such a prediction model and bring this to the stakeholder to the marketing people they always ask you immediately okay how can we increase sales what shall we do and now here it's important to understand that this is really a causal problem and and from a prediction model you cannot really read off what things you should do and this where we are um so here I can also tell we have some uh joint publications on this project so this was with noatis say started with the prediction model and then that's a problem. Okay, but somehow when we want to learn what drives our sales, it does not make sense.

### 01:11:51

**Martin Spindler:** So they observed that you have a prediction model for a certain product in Germany uh and then um a new data point come in you reestimate the prediction model but the variables which have been selected are quite different and and this is somehow challenging so we do not know what to do and here's the point is prediction models rely on correlations and for predictions correlations are perfectly fine but now if you want to intervene if you want to find out how should you do the resource allocation so in which channels you should do marketing you have a causal problem and and therefore here needs really to set up a a causal model for finding out how to do the optimal resource allocation. So you cannot simply from a prediction models by simulations find out how to do this and and therefore I like it because financial forecasting planning is usually one term but it's a prediction problem and a causal problem which need a different kind of modeling but but this of course also creates challenges to explain why you cannot use the prediction model directly to find out this and so on.

### 01:12:53

**Martin Spindler:** Uh but this um um I like because it really brings together this different kind of modeling approaches. Uh maybe I have a look at the uh time because maybe there are some uh other things I mean um what are typical problems? I mean marketing in marketing uh all um uh interesting all problems are causal problems and and in marketing mix modeling you would like to find out what is the effect of different kind of um marketing allocations on your sales and how you can optimize this and for this um now we have this traditional uh literature on marketing metrics models which are standard regressions and here uh we're working on a project with Google where the idea is really doing double machine learning uh using double machine learning for marketing mix modeling because double machine learning allows you much more flexibility and here uh coming back Martin to your question in marketing also of course dynamic effects are often important because you do an campaign then in the first um you have this ad stock effects where uh you have an uh dynamics in in the treatment effect.

### 01:14:07

**Martin Spindler:** So you do an marketing campaign and then in the first period it has a larger effect and then the second it might go down uh and so on but also marketing stock might pile up and and and this would be a first example where you have dynamics in your uh treatment effect and this then of course is a modeling uh problem and in marketing mix modeling you have some certain parameterized forms how to model this effects uh but as I said you can combine this uh with um double machine learning because it gives you more flexibility in this marketing mix modeling. Um so this is classicalally marketing mix modeling. You can also use this often. You would like maybe estimate retailers. You have an online store, you have offline stores. Uh how is the synergy between those? Um and and and for such questions, these are all causal questions where I think it's important to formulate this in this way and then um um use double machine learning to estimate this if you have really complex relationships or complex treatment patterns.

### 01:15:12

**Martin Spindler:** Then I mean here in marketing mix modeling you have of course a lot of nonlinearities at work. The other thing is you have a lot of heterogeneity and here for example the most important heterogeneity are seasonal components because you have this Christmas business uh and so on and here Kate with regard to the seasonal component for example it's very important and um you can as I said combine this with double machine learning uh to estimate this um uh effects but here also a challenge is that you have not only cross-sectional ID data but it's often time series data which creates some additional problems which is now also being developed. But I think this is an interesting development and uh I I uh I have a background in economics but I like for example marketing a lot because pricing uh marketing mix modeling these are all causal models where I think um this language is the right way how to describe the things how to think about things and here also in marketing mix modeling what are the right coariats to include and so on um are all also the first step and important questions which require uh lot of um modeling.

### 01:16:22

**Martin Spindler:** Um this were some use case. I still have uh one or two uh over but maybe we can then discuss this in the closing. So one is related maybe to a problem um uh Philip mentioned is for example how should you choose the markup to set the price because it's also a causal problem. So you if you present the price to a customer what you would pay you would like to know out what is the effect of this price you present on deal probability. so that he or she um uh does the deal. Uh and and now you have the problem if you uh set it too low, you might have a higher probabilities that you get it, but you lose money and um uh and if you set it too high, you might if you make a deal get more revenue, but uh the probability gets up. So this is a typical causal problem. Um um but we can then maybe discuss it closing and I also have one very interesting one where also difference and difference was used as a a strategy for pricing but um I do not want to overstretch your patience.

### 01:17:25

**Martin Spindler:** Uh so any case thanks a lot for the uh recap. Uh now I think we have a short break because online teaching is really stressful. So use it to relax. Uh get some tea, coffee or what is your favorite uh output middle fresh air is also a good one. Uh and then we meet again and then when we'll continue with difference indifference which is a widely used design you can use if you have unobserved confounders. uh and then um we have sensitivity and at the end as I said we can we have time for any kind of discussions and also uh maybe two three use cases simply to get you some inspiration how to apply this stuff. So thanks a lot for attention and then um see you after the break.

**Tsz Yan Lam:** Are we coming back at 11?

**Martin Spindler:** Yes,

**Tsz Yan Lam:** Okay, then.

**Martin Spindler:** perfect.

**Tsz Yan Lam:** See you.

**Martin Spindler:** See you.

**Daniel Jacob:** See you guys in a

**Sven Klaassen:** Okay, I think it's already start to share my Um yes so so can you see my screen right yeah great okay then yeah thanks um welcome back everyone so now in the second session we will talk about um one further model or specifically or another approach like Martin already told us on in in the toolbox right which I think some of you might might know already um difference in differences.

### 01:35:35

**Sven Klaassen:** But but the the main idea for us now will be on this session to to break down the basic ideas. What is the idea of different how and how can we apply it essentially for the um then in a double ML context at the end right we will see some some example of this and then we can after the break discuss the notebook which we'll be using definitive in detail on one of these examples. So of course as always if you have any questions or any points you want to ask or something you have from your use case what might differ from these things right just interrupt um me so so we we can just shortly discuss this or write in the chat if you if you would like okay for for different with um WML so so let's just start with the basics and motivations of course until now in most of these examples we've had a cross-sectional data right and you see this so so at any point in time we had n usually assumed like IID individuals like everybody's independently observed things like so so now we want to extend this or this part we want to use panel data or repeated cross-sectional data for for for this and how couldn't we actually estimate causal effects in these settings Right.

### 01:37:02

**Sven Klaassen:** And um for for for this um yeah you will already you can already see here how we will try to do this. So just as a first disclaimer um also with this panel data and um cause data we will usually need some sort of control group like causal inference as always is sort of a comparison right to to some suitable control group um or like we have assumptions so we from linearity things like this that we can infer some extrapolate some some um suitable values for some some other features. So we need some sort of control group and the same will be will hold true also for of course different diff other approaches. So we will have to select some sort of suitable units to compare our our um individual observations against but at first just a very brief I I will try to keep this one very brief uh recap on um panel data or repeated cross-sections. So, so both of these settings just to highlight are possible for for different diff methods. We will only focus here on panel data.

### 01:38:19

**Sven Klaassen:** But just keep in mind in principle these things also work for for repeated cross-sections. So what is the difference? Um in panel data you observe a number of units which is then called n over t time period. So every unit you observe at each point in time. So we have a discrete time setting, right? But there are no units which are just observed at certain points in in time values. Sometimes units drop out but essentially it's it's a continuous time series for for a specific unit compare that would be something if you have a longunning business relationship where you have repeated interactions with the individ individual, right? And the repeated cross-sections instead is usually a a subsample, right? At each point in time, you observe a subsample which might be different or might include the same individuals but but there are just indiv you have at each point in time a subsample of your whole customer base customer population things like this. So yeah just as a visualization cross-sectional data we have n observations we observe usually features x treatment values outcomes right and for panel data we observe this not only for one unit uh for one time period but we observe this for multiple time periods specifically for each unit we observe all these values of over time right all these this whole history Of course, the values of X can can sometimes be time fixed,

### 01:39:59

**Sven Klaassen:** right? Or should be to some degree. And the the difference to cross-sectional data or repeated cross-sections would be that at different points in time, we just observe a corresponding subsample or of course depends on the data size, right? But sometimes we observe units twice, sometimes just on a single time in some time period and things like this. just a subsample of these and just not to compare uh to to to compare to to time series data and time series data we observe just a single unit over time. So so this just just to clarify what what these the these uh differences are. I think it's that's quite clear but if there are any questions on on this maybe we can discuss this now. So so what we want to work with now is or conceptually is is panel data. And the the main idea is of course now we we have not only one observation but multiple observations and this has a of course time complicates estimation, right? But observing the same unit over multiple time periods also allows us to to actually um get rid of some unobserved confounding factors which we will see um in a bit essentially.

### 01:41:21

**Sven Klaassen:** So this is also from a causal perspective usually very helpful and the basic idea for this you can already think about is of course if I observe the units at multiple time points right I can compare the unit to some degree to itself at a previous point in time right so so so you so you can see something of on of on of on of on of on of on of on of on of on of on of on the what what happens at the level of the unit what happens whether the level of outcome changed or something like this for for the same unit. Okay. So now um just just starting with the actual topic. So so what is what is difference and differences um and the the idea is again to to have a toolbox which tries to estimate some causal effect or in of of some intervention. And the main part like I said for any cause and inference method is to compare some some treatment group against some control group to to find suitable controls. So, so how do we design them in um in um the how do we design the corresponding counterfactual?

### 01:42:35

**Sven Klaassen:** what what would have happened without treatment or what would have happened with treatment, things like this. And and the um the basic idea is that the control group we we don't consider the actual outcomes of the control group, but we consider the trend of the control group and the the trend would be the the change in outcome. So the the change in outcome or how the outcome changes over time for our control group. That's sort of the the trend, right? Is a proxy for what would have happened for for the treatment group in the same same direction. So how that the treatment would have changed and we will see in a short uh shortly that this is this is a bit different than just assuming conditional exogenity in in the these basic settings. So, so from a visual perspective, um we we have two different groups. So, a treatment group and a control group and they consist of multiple units, right? So, so it's not a single unit, but on average we we see on the right side in the plot we see the average over time, right?

### 01:43:47

**Sven Klaassen:** For both of these these these groups. So, the which one we will call the treated group, right? And the other one in this case we will call because we it's later the never treated group right and so so in in both of these groups we see on average what the the outcome is in this example. So here this is actually some logarithm of um unemployment and these are averages or the the unemployment rate in different states or measured in different counties. Right? So so you have multiple counties in the US states and then you you you have on average some some unemployment rate and there was a change in minimum minimum wage between in this period between 2003 and 2004. And then maybe the question would be whether this change actually had an effect or how can we estimate this this effect of on the unemployment rate and um like I said we we have two groups. So so the orange one is the one which received the treatment and the the blue one did not receive the treatment.

### 01:44:54

**Sven Klaassen:** But of course like we can see they are already for example on a completely different level right. So so we cannot compare them directly. So we can't say in principle we would expect for for for for the orange group to observe this value over here right as a control group and instead um what this does is um so it it tries to capture the the changes over time and that's why it's called difference this one that's where the difference part comes from from from the difference and difference estimator between these groups. So what we will do as a as a comparison uh we will consider this one here to construct our counterfactual but only with changes over time the the the the blue line over here. So I need to oh I would like to introduce some very a bit uh notation to to just highlight or to to to just be able to to write down some some of the basic ideas. So usually we will break down all these things at first to a two times two period. So comparing two time periods, one before the treatment, one after the treatment, two time periods.

### 01:46:10

**Sven Klaassen:** So so and just with two different levels of treatment. So now we have um a pre-treatment period which we usually call T0, right? And a post treatment period T1. So could be at a later point after the treatment but just a two times two setting and we we observe for both time points we observe the outcome for each unit and we observe an indicator whether the unit gets treated between right T0 and T1 right there's some sometime in between there's a treatment point whether the the the unit actually got treated and then we can obser we can define sort of potential outcomes correspondingly saying that at each point in time we have a potential outcome if the unit or if if somebody gets the treatment or not. So it's it's really the same setup as we had yes uh no not yesterday last week right that that we had last week right saying what are potential we have potential outcomes so so we have factuals and counterfactuals right at different points in time so for the treatment group we observe these potential outcomes after the treatment for the control group we observe these potential outcomes after the treatment right so the question is how how can we constru construct or on principle the other one the the the counter factor right from this part and the goal is what we would like to estimate in the standard average um different estimator is the average treatment effect on the treated so we had this also very shortly in in the

### 01:47:54

**Sven Klaassen:** heterogeneous treatment effect section so so it's a specific type of gate so so it's the treatment average treatment effect for the group who actually got treated, right? Not not for everyone, but conditional on actually being treated, right? So, so just a group indicator for the ones who actually received the treatment. And the the idea is um is or what what how we would define this is essentially for for for the treated group that was the orange line. If we take a look at two time periods just just before and after the treatment right just directly before and after the treatment then we observe what what the potential outcome for the treatment group on average before the treatment and we observe what happened in time 0.1 so y1 right the index one just after the treatment what is the potential outcome with treatment for this group so this this orange point is the one we observe And what we would like to know is the counterfactual on average, right? So, so just the in time point period one, what would be the the the potential outcome without treatment but for the treated group, right?

### 01:49:13

**Sven Klaassen:** But for for the ones who actually got the treatment, what would be this difference? Uh and and the difference between these points like how whether they differ, that would be something which we would call the the average treatment effect, right? on on the treated in this this time period and the same setting you can then extend to later periods. Right? So if you think of the these points in a later time how they differ or how they change over time, how how they they look after multiple periods. Um yes.

**Ani Pole:** Um I have a question. So it makes sense to compare before and after and but like the way we think about this is sometimes in a discrete manner before and after. However, like time is continuous. So like um when after the treatment do we do this evaluation? Like I I guess this depends on context, but

**Sven Klaassen:** Exactly. Um yeah, you you can do it on in multiple points after like like usually also your measurements are discrete, right?

### 01:50:15

**Sven Klaassen:** Uh in in time of course you you can do it in a at a very um fine grain level or a higher a larger more roughly grained level.

**Ani Pole:** Um

**Sven Klaassen:** But you this is just a two point um two design. You can do the same evaluation then one step later, right? You you can just take different points and the effect can be different over time, right? It can you you can could have a effect which is small at the start and then just starts to increase or you could have an effect which is just flattening out, right? Or you you have an early early adop effect that that there's a change so people react to the change but after some time it's not new anymore. So so people just the effect is essentially back to zero. So, so you you you can just evaluate different points in time. So, so, so the T1 just means it's after the treatment doesn't mean how long after the treatment. So, for different combinations, you get sort of different effects after different point points in time.

### 01:51:16

**Ani Pole:** um sorry Martin just like one last followup. So um when we do difference in difference then how far back do we go to basically establish that um kind of like the difference between before the treatment uh and then to use that in our evaluation of getting the uh average treatment effect.

**Sven Klaassen:** And then that that's a a very good point. May maybe we can come back to this if we have like the multiple periods and we can see because that that that it's actually something you have to be a bit careful about. Um but but if we maybe if we have this for multiple periods we we can go go more into detail, right? Then then to play like like how how much now it's just like one period before one period after but of course all these details how long it before and things like this ma matter to to some degree right yes but so and uh

**Ani Pole:** Got it.

**Sven Klaassen:** Martin you had Okay,

**Martin Bierey:** Yeah,

**Sven Klaassen:** cool.

**Martin Bierey:** I was just wondering to the question how many periods after I mean if we would be super strict believers in the common trend assumption of the treatment and the control group could we even identify it in a datadriven way because like if their trends are really identical then we would assume that their trends only diverge during the period where there is a treatment effect and then their trends should be similar again or is this is this too strict?

### 01:52:44

**Sven Klaassen:** um the the the the effect can be uh the the treatment can have an effect on the trend also. Right. So so it we we can like you said but like you said isn't if if we try to evaluate it for multiple time periods afterwards we are assuming the trend holds for a longer time. It's it's I I want to I I will will show the what what the trend assumption actually means and and then like if we we increase these periods it it gets stronger and stronger right to say like they they would behave parallel over a very long time right even after the treatment and and then usually to evaluate these different it's more plausible to have short-term effects than very long-term effects overall that just as a very short summary um from from this and the longer you try to estimate these effects the more restrictive sort of your your your your comparison becomes and more restrictive essentially your assumptions are. Okay. So this um from this very formal representation and um the basic the basic idea for for this let me see um yeah I we we have this here for for for this one I I just want to go back the basic idea is that instead of thinking about that we compare it to the blue line what what happens in differentive is we move the blue line or the the trend of the blue

### 01:54:23

**Sven Klaassen:** line to to to the orange line. So instead we assume the orange line would have followed the same trend as the blue line. So we could in our mind draw something like this here, right? That this would be our counterfactual which behaves just in parallel to the blue one. So that's that's called parallel trend, right? So it just behaves as the blue one but at the level of the orange one. So the trend is the same if we have it but not not the the the overall the the the overall um values are the same but just the trend. So the changes over time that is that is the main point of defendive. So if we take a look at the exact formula for this. So this is called the and this is what m Martin um said at the beginning. There are assumptions like unconfoundedness which help us to identify these effect to say we can identify the causal effect and the the um the for different the identification assumption is this parallel trend assumption.

### 01:55:29

**Sven Klaassen:** you can test it to some degree. We will see later. But this is basically an assumption and this is just um so sort of which which you assume to say okay if this holds then my then I can identify my effect and the the the um the assumption says that in if we don't have a treatment then the change or and change is a trend right. So, so what how the the the the values change over time determines the trend, right? So, so the change is the trend. So, the change in the outcome for the treated group would have been the same as the change on average for the control group. So, it the treated group would have had the same trend and this what what does it mean that this is a change you can see here for the control group, right? This is this this this difference over here you this is just a difference between both of these. So it's a change and this is what we would call trend in this example.

### 01:56:34

**Sven Klaassen:** And the assumption is that this change over here is the same as the change for this this green line right because the green line we don't observe that's the counterfactual and the parallel trend assumption says that the the change so this difference both of these differences here are actually the same that that is that they on average this difference between the the the the point over here and this point. So the counterfactual one is the same as the difference between this blue point and this blue point. So they have the same change over time. So they have the same trend. So it's sort of right having this change and trend sort of interchangeably but that is that is called the the the parallel trend assumption because I can observe how the the outcome changes the orange one. So the change the trend for the treated group but I can't observe how the how the the the trend for for the counterfactual and the probably trend assumptions as the trend for the counterfactual this is change is the same as the trend for my control group and then I can for both of these if you think I can just take this difference subtract this difference I'm left and I'm left with the the the the the the difference in this example.

### 01:58:01

**Sven Klaassen:** So I I know there's a lot of formulas in these these parts to to say but this tries to explain why this is called a difference in differences because each trend is a difference right the trend for the control group is a difference between the blue point before and after the treatment. So this is the trend for the control group. The the difference between the for the treated group or the trend for the treated group is a difference between the orange point before and after the treatments. So the this difference and if you take if you subtract these differences so you take a difference of differences you you you come out with this effect or the difference you see in this example. So, so the par and I think even with all the notation this is to some degree I think quite helpful in the the visualization that you you can see okay why is this is a difference of two two differences right but one difference the green one we don't observe right that's the one we we don't know because the green line is some counterfactual we don't observe what would have happened without the treatment and the identification assumption this parallel trend just b it really means you can see is that this the the never treated units on average or the trend from them would have behaved the same or behaved the same as the control units so instead of using this unobserved difference I can use this observed difference so so it's

### 01:59:44

**Sven Klaassen:** yeah on a very u very detailed level here so but just to explain what is the basic idea from difference and differences So from these assumptions we can we can write and this is on this formula. So so the the parameter we or the the parameter we would not want to know is a change in the treated group. So a difference for the treated group minus the change in the control group. So a diff like I said difference in differences and really this is some the question is whether this assumption is reasonable right. So, so whether they would have behaved the same over time in exactly this this this fashion because this has really not you can visualize it nicely, right? You can draw these lines specifically and then you can show how large these changes are. But um we the question is for example how can we know whether the control group would have followed uh the same trend as a treated group right or vice versa for for these examples and I I don't know maybe you all already know but the is the the main idea from from this difference and difference is then to to also include coar periods because this one here, we won't need machine learning for this, right?

### 02:01:10

**Sven Klaassen:** That's just an average for my that's an that's an average for my treated units after the treatment. That's an average for my treated units before the treatment. And here the same thing for the control group. So I don't need any machine learning method. I don't need any estimation really. I just compute averages and I subtract them, right? And then I would would get my my final effect. So the question is for for different for for this usually this parallel trend is sometimes not completely plausible. If you think of the states example, um if you compare two US states and they they might be completely different, right? And how how the decomposition of of of the counties, right? So so there might be more rural counties in one state and more urbanized counties in another state, right? That the their complete or the the population density things like this uh but is is different in both of these states much largely. So, so you wouldn't assume that on average they would have developed the same, right?

### 02:02:17

**Sven Klaassen:** The the trend would have been the same for both of these states. So, the the idea would be that that instead of assuming these they would have developed in parallel just on on the overall average you would say okay just the conditional conditional on that being on the same organization level, right? or the same same level of population or same level that they would have be be um behaved the same. So you would just compare like heavy um urbanized counties to other heavy urbanized counties in both states and then you would rewe them to have the same proportion of like urbanization um population level and things like this. So this is usually a bit more plausible assumption to say okay we want to have something like conditional parallel trends. So conditional on our features X right and X now is something like our confounders right. So, so you have a set of confounders X which influence our outcome and our treatment, right? And you want to say I condition on these relevant facts which affect our trend, right?

### 02:03:28

**Sven Klaassen:** Everything which affects the the development over time in my outcome and in my treatment. I want to try to condition on these and then I say okay I compare then then it's much more plausible to say that these conditional trends in these these these counties would have developed similar over time. Yes. Uh there are two two questions. So so I

**Tsz Yan Lam:** Yes, I'm a little bit faster than Martin,

**Sven Klaassen:** don't

**Tsz Yan Lam:** so I I will go ahead. Um, so I I I kind of understand the idea, but would you even say if I really want to do something a little bit more maybe too complicated, but I can try to build a time series model on the control group to use the uh before treatment and then try to predict what is the after treatment. So both are observed. Then I I build a model. Then I apply that model on my treatment group. Then I create this well kind of artificial counter counterfactual, right?

### 02:04:33

**Tsz Yan Lam:** And then using that to say that is my treatment effect. Would it be the same? And then whether it is actually something that are making it too complicated.

**Sven Klaassen:** uh and no no so so so no not too complicated I I think the the basic idea for for this um is of course valid to say okay from my pre-treatment periods I want to estimate what would what would have happened right without my um treatment so so but what it wouldn't be able to to capture is something like the um time fixed effects, right? If if you know from panel data, there are things like um and we will see later this this accounts for individual and time fixed effects. So so in a two* two setting with linear models, this is identical to two-way fixed effect estimation just if you you want to compare this. So, so and because there might be some time fixed effects which depend on on um which affect your control group and your treatment group, right? And so, so in your time series example because you you can't um usually if it's not predicted in the trend, right?

### 02:05:48

**Sven Klaassen:** But so sort of it's if you if you don't get the trend prediction of your time series is completely correct because it changes because the overall there are some economic conditions which change or something like this then you would attribute these changes assuming you would previously predict just a simple linear trend right then you would just follow this linear trend but if there are some changes in conditions that this trend just turns downwards or something like this but this has nothing to do with your treatment you would observe it in your control group. So these changes would also be measured in your control group. But in the other approach, you would attribute these changes to your treatment, right? So so you would they but if you assume these things the trend and the overall example holds it. I think it's it's still right a practical approach, right? Of course in all these examples like the there's like there's no no perfect solution, right? to to to have the the the perfect control and example. So in some cases that might might be valid or on short term or things like this to say okay I I want to try to predict things in these simple examples and synthetic control is something we won't talk about is is very similar on the method what you are talking about and it works more on a time series level but it uses uses also a donor pool.

### 02:07:13

**Sven Klaassen:** So, and the donor pool corresponds to the control group in this example, right? So, so it uses this this control group, a comparison group um as a as an example to say, okay, what would have happened to account for these these time time changes afterwards?

**Martin Bierey:** Um yes I have a question on what you just mentioned here with the so so you described this parallel trends assumption as something that that we think about conceptually and then if I understood you correctly then we would also say maybe we have control groups where the co-variants are similar to the treatment group and then our different treatment effect is conditional on this co-variant um c can you help me explain why so if I would think very naively about it then I would do something Like so if I have a lot of candidates for the control groups, I could just basically look at the data and say which ones had common trends in the outcome variable in the pre-treatment period and then I wouldn't explicitly look at their co-variants or anything. So maybe you can help me un explain why here we would do it more conceptually and maybe go into similar co-variants instead of looking at similarity of the outcome trend in the pre treatment period.

### 02:08:34

**Sven Klaassen:** Um, yeah. So then then I I think what you described is is a completely valid approach to and that's more or less what synthetic control is doing. Synthetic control is trying to fit on pre-treatment periods the outcome trend as good as possible and then tries to to to um to and but also uses usually then co-variants to to try to to fit like get a better fit on on or plausibility on what what the the decomposition or or comparison of of of control units would be like I I don't know if you if you know synthetic control in these examples. So, so and and there the the the same idea is to you you could just uh use synthetic control without

**Martin Bierey:** Yeah.

**Sven Klaassen:** coariantss, right? In in principle you could just fit the outcomes and try to set weights to to without coariantss to say okay these weights then determine uh are previously a good fit. But with the coariantss all these um parts on predictions become more plausible on these underlying um conditions right then then you assume something like the the the features are something like gen you're trying to describe some sort of economic conditions in these examples and and whether they they change and you try to to rewe them over over these times to get more similar units to compare actually

### 02:10:05

**Martin Bierey:** Yeah,

**Sven Klaassen:** against.

**Martin Bierey:** I I was thinking they don't necessarily need to be synthetic, right? So, for example, what we sometimes have on our B2B site is we have 100,000 users, right? And now if you want to treat 50, you have a huge pool from which you can select.

**Sven Klaassen:** Yeah,

**Martin Bierey:** So, so you don't even need to do it synthetic that you just take proportions, but you can take actual users and basically find groups that would have behaved very similar and and then it's probably somewhere in between. Um, okay.

**Sven Klaassen:** that that is somewhere in between. I I still think to to not overfit um on on the outcomes which happened to be is very similar using specifically coariantss is usually very helpful to to also get these um overall trends and the the if you you're using then a sort of matching approach just right it like like all of these is more or less a spectrum right on on what one is using right and the the the the um and the the matching part.

### 02:11:11

**Sven Klaassen:** So so the idea to also fit on these coariantss would be to fit units which are in the background characteristics also similar that you don't observe which are then correlated to maybe not only the outcome but X features X more or less. So so you you're more it's more helpful or more plausible to think that these units would behave then similar over time and you're not really overfitting what actually because usually outcomes are also very noisy, right? Um, so so you're not overfitting on the outcome what what the actual features there are. But I think in principle it's it's possible to to just use outcomes. But the question is now how this then performs depends a bit on on the data. Okay. Yeah. But very very good points. Um okay. So, so this was the basic idea of parallel trends in um in in this very basic two* two setting, right? To see what what actually how is this estimator done, how are they described and what are we comparing of these examples.

### 02:12:22

**Sven Klaassen:** So usually we have in these all these examples multiple time periods. And how these multiple time periods work is you you um um you usually want to have um different treatment effects after the the the evaluation. So here we have just the treatment in this time period but the effect might be quite different in 2005 2006 right and the the later points in time and typical panel data models usually don't have these examples except if you add a lot of interactions you have to design these features a bit manually things like this and um these these periods are usually helpful you already mentioned to some degree like the pre-treatment periods can be used as placebo testing, right? to say whether trends actually developed in par developed in parallel before the treatment actually happened and then if you can can say say something whether it's plausible that the pre these parallel trends already hold that doesn't mean that they would have developed parallel after the treatment but I think just because call the inferences a basic idea of what is plausible in assumptions it's it's usually a very important tool to to to compare.

### 02:13:49

**Sven Klaassen:** Um and what is also possible you you can have multiple treatment groups which are treated at different points in time which we will see see later. So, so for for for this um we will use this basic notation over here and I I try to go through these assumptions just on a high level because I think the the assumptions just the basic idea are the relevant ones for for this what what is the basic intuition behind usually these assumptions or what are they what are what what happens if if they don't hold or what what what would be sort of the problem why we need them theoretically play and for for most of these settings the the idea just to clarify it the out we have the outcome for unit I observed at different points in time so we have two indices right we we have a group indicator which denotes when the unit is treated first treated so if it's infinity it says it's never treated so this is you this is our usually our basic control group that the units which are not treated at any point in time but the idea is that units can be treated at different points in time.

### 02:15:01

**Sven Klaassen:** So we need this sort of we divide them in certain groups and um still we have a treatment indicator D right they they are slightly different this is a time point when you get treated and this is actually whether you are treated at a certain point in time so so this is essentially this indicator function then we have some covariants which are usually pre-treatment coariantss which are used again So we don't get these feedback effects right that our outcome affects our coariantss and things like this. So it's usually exogenous coariantss or pre-treatment coariantss for this trend and some set of time periods capital t and the the first part which is a bit more complicated now because it's also what what you asked to some degree which points in time do I want to look at right that was already the question right like like time is continuous which point in time do I actually want to look And therefore the we don't don't only have one treatment effect right we have just a complete um multiple treatment effects for each point in time we want to evaluate and they could be in principle different for each group like remember the group is when you get treated right maybe in time in January then there's a group which just gets treated in April and the the these effects for both of them might be different at different points in time.

### 02:16:36

**Sven Klaassen:** So we have all these combinations that we have a treatment effect for each group at each point in time. So we have two different indices which tells us when does somebody get treated and in which period we are evaluating the treatment effect. So so all these type of combinations which which which we try to to um consider. M yeah,

**Daniel Jacob:** Yes,

**Sven Klaassen:** that's

**Daniel Jacob:** we have a question. So you also said that the um treated group po post treatment um can also have a so the effect of this treatment group can also change. So they can kind of develop a different trend if we're now observing multiple periods. Um kind of my first intuition with having these multiple periods would be to observe the treatment effects for the

**Sven Klaassen:** Um

**Daniel Jacob:** treated based on time. So they can maybe say ah in summer months for example they are higher than in than winter months. But when we also assume that the effect itself or that the trend can change just maybe because in period one they have the treatment and then now in period two based on this treatment in period one they observe kind of another trend or develop another trend.

### 02:17:54

**Daniel Jacob:** How would I distinguish this? How would I really say it's just because of the time and not because they have now treatment for like multiple um periods?

**Sven Klaassen:** so so so this in this or I think conceptually this then belongs to just the treatment effect because it's the change like even if they now start have an accelerating trend would mean sort of that at each point in time your effect gets larger which which would over time manifests as an accelerating trend or at each point in time if you have a negative effect your trend gets gets then slopes downwards or things like like this for example. So so because as a comparison group you would you would still assume that without treatment they would have behaved have the same trend as a control group. So so they would have the same development over time as a control group. So all the differences you observe in these parts are essentially to the treatment. So they are all called treatment effect but it's not decomposed into sort of some first effect plus some trend or something like this.

### 02:19:04

**Sven Klaassen:** It's just different points where you have this

**Daniel Jacob:** Yes. Right. Yeah.

**Sven Klaassen:** treatments.

**Daniel Jacob:** Makes total sense. Yeah. Thanks,

**Sven Klaassen:** So so what what is the difference from this the previous two* two setting? Um so so like I said we have all the combinations. So it depends when we get the treatment or when treatment gets started with the combination and at which period the effect is measured. So so over time which we will see in this. So so this is a very flexible setup right because we have all these combinations. So so just this is how um different diff really differs from the panel data methods. So if you are a bit familiar with panel data methods, you you have us really some sort of linear type models which assume some linear structure over all these time periods. You can include some interactions, you can make them more flexible, but you have to construct these things specifically manually to to to allow for all of these type of effects and they are usually assuming some linear structure also in the coariat some linear structure over time in the effects and like this.

### 02:20:16

**Sven Klaassen:** So this this is how how these things differ from if you're applying sort of these standard panel data models. So going through these assumptions I um I would just very shortly get get sort sort of the the the the intuition what we assume. So so the first part is the the treatment is sort of irreversible. So in this part staggered adoption. So if you get treated, you stay in the treated group and that's just from from the part conceptually that you don't forget that you got treated once, right? So so so the treatment actually means that you got the treatment once or at each point in time that might be different types of treatment, right? So so whether you got got some favorable conditions once and see how this affects you over time does not mean that you get the same treatment at each point in time again. Right? So these are different things. So so just that it means so so you don't you you have some sort of memory to remember that you actually got the treatment once and this is what you want to evaluate in these examples.

### 02:21:27

**Sven Klaassen:** And then the second one is is as is panel data right that that we have this type of panel data. We have individual units from which we observe this whole history right this whole history of data. And um oh I sorry was the wrong direction. And the second uh the third one is that we don't anticipate being treated. So so what this usually means that units don't change their behavior before the actual treatment is assigned. Right? There are things how we can handle this which we will see if if this doesn't happen. But in in um the the basic idea is of course that if units already change their behavior before being treated because they know that the treatment will come then what would happen in principle if you we go back to the slides in the two times diff setting in the graph is that this green and orange point would be different right because the green point is essenti is the the potential outcome if you get the treatment but because you change behavior already before you get the treatment.

### 02:22:37

**Sven Klaassen:** The the these trends already differ in previous time periods, right? So so so so the counterfactuals you you already change your behavior before the treatment. So so in this part the the green one is the counterfactuals without treatment and with treatment and that they are the same point actually means you don't anticipate you don't anticipate that you will get the treatment in in future time points. So, so this is this is the the really a very clear assumption there. Um, there's a

**Ani Pole:** Yes.

**Sven Klaassen:** question.

**Ani Pole:** Um why couldn't we then use uh the time of being aware of the treatment as kind of as the period of the treatment?

**Sven Klaassen:** Yes,

**Ani Pole:** So like

**Sven Klaassen:** we we we can we can that is this what is actually done. We we just shift everything, right? Like we we shift everything like one period back, right? So, so we we or it it depends on what you would like to estimate but yeah you you shift okay the solution how to handle it is usually you try to shift it as much in the the past to or and that you would say okay now it's plausible that nobody anticipated being treated right and then you can try to eval evaluate how how how this affected your your your changes right uh but it it's a quite simple type of solution but I I I think just to be aware that that usually of course still things are not

### 02:24:02

**Sven Klaassen:** perfect, right? And it's just approximations to to the the truth there. But um yeah, on a yeah, often it's yeah, it's it's unknown whether people anticipate but but you maybe have some idea whether these things change a bit. We we can see this in the notebook in in we will see some example when when it's very obvious to see what what happened then maybe if your placebo test just fails one period before actually getting the treatment that might be might indicate that you have some anticipation effects right that that people already just before the treatment are already shifting their behavior. If you have multiple placebo tests which estimate zero effects and then just before your treatment you estimate an effect that that that might indicate that the people already changing this. Um the and the the the fourth one and this is the base the the really the important one right the the really important one is this conditional parallel trend assumption. So so and this means conditional on this coariant X. So, so in subgroups with the same features, I think of X always as subgroups, right?

### 02:25:15

**Sven Klaassen:** If you have subgroups with the same characteristics, in these subgroups, the the change in outcome is the same as the change in their control group. They they they have the same trend over time within these subgroups. So I think from a practical point of view is usually what you want to include as coariantss is really to to think about when I condition on these coariantss and units have the same same age the same type of um or or in on on high levels you have comparable units then they should have behaved similar over time right on a similar level And this is or visualized in this example this would mean in in this parallel trend what we in principle have talked about this is the parallel trend assumption unconditionally right unconditionally if we don't have it in subgroups but within each subgroup you have the same type of assumption right so so if x is just two different groups right urbanized regions and uh rural region regions right you you just make a binary binary variable to distinguish between Then for each of these type of regions this assumption would say okay the the the the green line the counterfactual would have followed the same trend as the the the blue line right and this means you you're conceptually just moving it right in as a parallel trend and you would assume your counterfactual looks like this.

### 02:26:49

**Sven Klaassen:** You can see it's parallel to this one. So the changes are the same over time. So that's why it's called parallel trend for this and yeah there are different types of control groups you will see later. So so you can usually a specific group is the ones who who don't get treated until the end. Right? But another one you can use is usually the ones which did not get treatment yet. Right? And that's sometimes a bit more plausible. Sometimes you even want to exclude the units which are never treated because maybe there's a reason you have that they are never treated and they're they're from they're quite different from your actual treatment group, right? They they behave quite different from your actual treatment group. They don't react to anything and they have really different characteristics, really different buying behavior, completely different structure. Then then you might want to use just units who who get treated in a later point in time, right? In two or three time periods later.

### 02:27:56

**Sven Klaassen:** Maybe you will just want to use them as your control group because they are more similar to your treatment group, right? Because usually you want to have something as a control group which is as similar as possible. So your parallel trend is as plausible as possible, right? So so in similar with all these type of characteristics. So, so these are the typical choices to say the not yet treated units or the never treated units you want to use as a comparison group to construct your counterfactual. And of course, we also need some overlap assumption or common support assumption because we want to have this. So, so we want to infer something for the pro for the um we have the conditional parallel trend but to estimate the conditional parallel trend we have to already observe everybody in the control group uh for everybody in the treated group a correspond at least some corresponding units in the control group. Right? In in synthetic control that would be that we have similar units actually available and we are not extrapolating but finding something some units which are similar where we can really um compare to in these examples to to actually have have treated you and untreated for each treated unit we have untreated units available which are comparable.

### 02:29:21

**Sven Klaassen:** That is what this assumption this is an overall summary for for for this one. Um, I hope I know for for different and diff it gets a bit complicated specifically with with multiple periods, but I hope the the main ideas or the the main points were were clear and um but there's still one sort of not not big issue but one part actually um um relevant is that we want to estimate this treatment effect for some per evaluation period. period. Right? So if we go back at the graph, right? We want to say maybe in 2005 we want to estimate the treatment effect. Right? So now the question is which trend are we using? Because we can use the trend starting in 2003 something pre-treatment, right? The trend from 2003 to 2005. But in principle we could also use the trend from 2002 to 2005 right like like we could estimate the both are valid right like if you assume the trend holds over the whole whole time but they are just two slightly different um correspond to slightly different assumptions.

### 02:30:44

**Sven Klaassen:** 2002 would mean that the trend from 2002 to 2005 is actually in parallel and 2003 would mean just from 2003. So it's a bit less restrictive, right? So you see like the comparison the the we can have different points in time to compare to. And what we are usually doing is we are using the shortest right the shortest time period possible to estimate the trend because it's usually more plausible for the trend to be in parallel over shorter time periods than than over a very long time. Right? So but what one can see then directly is that if we try to estimate for example the effect in 2007 we still have to use at least 2003 as a baseline period right to to start from the the trend from right because we have to see what happened before the actual treatment as for the trend right because the trend afterwards can change so that's why if we are estimating treatment effects far in the future right over long time periods It's our trend assumptions get stronger and stronger, right? We are saying okay the trend was parallel like from 2003 to 2004 they are similar maybe it's plausible right but that they are still similar to 2007 right over very long time periods gets less and less plausible right so so so that is just if you estimate treatment effects over longer time periods that is just be aware that this is always corresponds to your your assumptions getting stronger and stronger for that that you you you compare to and

### 02:32:24

**Sven Klaassen:** therefore what we um then this this can be identified then when a cert with a certain moment equation but this depends not only on the the time period I want to estimate and the group but also the pre-treatment period right so what I said we want to use the shortest pre-treatment period but you have always three a combination of three parameters you are estimating for a group for a pre-treatment period and for a post treatment or evaluation period you want to estimate. These three type of parameters determine which effect you're you're actually estimating. So the effect only depend should only depend on the the group and the evaluation period. But the strength of your probability trend assumption depends on which pre-treatment period you're actually choosing. And this is automatically set usually to the shortest one. But you can compare them for all of these. So to compare or to come back to the double ML part is what what what are the machine learning parts we actually have to estimate from this part to for for for this or what double machine learning needs to estimate.

### 02:33:34

**Sven Klaassen:** So we need to estimate the conditional trend that is the part which we need. So we need a regression model as we've seen before. So we need one regression model for each setting. And this tries not to estimate the outcome conditional on X but estimates the difference in outcome. So the trend right we we will use the outcome model is not actually estimating the the outcome but the changes in outcome. So to really try to predict the trend we have one one model which predicts the trend that is usually called in this part G0 because uh for so one regression model and we need a propensity score. It's the same part as before to to estimate the probability of actually getting treated or not not getting treatment to to get our score and to reweight things correspondingly. So like in the really the same actually the same as in these um average potential outcome models as in the interactive regression models right all of these we need one outcome regression which which just works on changes and one propensity score for for this.

### 02:34:44

**Sven Klaassen:** So, so just to to summarize this um so so we want to estimate average treatment effects for certain groups at um for group so depending when they get treated at different points in time. So we have all these combinations and this basically uses we need parallel trends or conditional parallel trends that is the main assumption and limited anticipation right that that people really are not changing their behavior too much before right or not not as much for for this then then we can really create this moment condition and we we not need to estimate the the change or the the outcome conditional on X and the propensity score this is done with the double ML part or the package and also if you're using some different diff package in R like different diff in R this is with with doubly robust estimates is actually using the same form of estimation maybe not with a machine learning model maybe with some linear regression and logistic regression but again using a linear regression for this model and losing a logistic regression for this part of the So, so same same form and then we we can use crossfitting and try to do all the same procedure as as all the these same parts to.

### 02:36:11

**Sven Klaassen:** So, um we will see this any any questions to to this one before we we we see one example here. Um but

**Daniel Jacob:** Yes, maybe. Um, so since we were also talking about the assumptions, I think one of the assumptions is also that we don't have any uh spillover network effect. So this basically super assumption and I wonder um so the idea from can earlier saying hey um how about I'm developing a time series model um pre-treatment and kind of try to figure out what would

**Sven Klaassen:** Um

**Daniel Jacob:** what would be the trend. Could I also somehow use this in order to detect maybe any spillover effects? Because I could imagine especially like in our cases where we are often dealing with products where we have um kind of a limited or um fixed amount of units or or demand when we make changes to some of those products um there might be those spillover effects to control groups and so on. Do you guys have kind of experience with this especially kind of in this um time series setting?

### 02:37:21

**Daniel Jacob:** I was wondering if there would be some ways to to identify this better. Um, yeah.

**Sven Klaassen:** I I think for for spillover words it gets really complicated really um strong. So, so I usually I think for practical reasons I will of course if the spillover effects are large you have to do something but if they are you think they are quite small I think it's usually fine to run a working model to say okay I I think but which which sort of tries to to say okay spillover effects are neligible in in this this but um I I think if if they are um the problem is then some sort of then you get really fast into identification problems if you don't assume a lot of things because you can't distinguish spillover effects from um time trends or time changes like time fixed effects things like this you can't really distinguish them or also or yeah maybe from time fixed effects to some degree yes but so so for for um for for the the spillover for these effects because your control group is is affected right from from these changes.

### 02:38:36

**Sven Klaassen:** You you your you your the whole identification for these assumptions breaks down because you can't use them to say what would have happened without treatment. So, so, so you um you're estimating a a combination, right? You depends a bit when when you say like the spillover effect, I I would say if you say the spillover effect would increase also the sales of the part in the other models, then you're underestimating your effect slightly, right? If it's the other way around, you maybe overestimating your effect slightly, right? So, so may I I would try to maybe go a bit more in this practical direction than just model everything there in detail because usually like really working with spillover effects with with any time is is usually without these you you need more structure on your problem. Usual usually say really something about what

**Daniel Jacob:** Yeah, thanks for thanks for elaborating Sen. Very interesting. Yeah.

**Sven Klaassen:** And um so so I would say something about how this would actually look like and we will go through this one other example in the notebook then in detail right.

### 02:39:57

**Sven Klaassen:** Um this part we had already and um the what what is the basic idea of if we have one example so how does the data look like? how can we implement it in a what is the output we are getting if if we are comparing this. So um in in this example we we are using this minimum wage example and this starts or the data starts with with the the um long format. So the important part is we have our time variable right which in this part is just have an identifier which or identifies our unit and this part these are the counties right for for these count for for these states and um we have this variable group variable which says okay in which which time period would this county get uh treatment right so this one would be treated in 2007 seven. So it's it's it's in the part actually is not really used and we we have something like the the outcome and population average pay in the in the corresponding have region indicators the same. So what we are then we don't um need to specify or what we need to specify are all these type of features like in the the other part where we only need to specify what are the our controls what are our outcome and what is the treatment here we need to say okay we also need what is the outcome variable what is the um the treatment variable so so this is the the column G when the unit gets first treated right the first treatment period say just as

### 02:41:48

**Sven Klaassen:** a time point in time not 01 but point in time and then the the um what is the actual time we observe so so what is our time column and what how can we identify units so the the changes are mainly these two columns we need right we need additionally a time column to have panel data and we need to identify which are the units which belong together right which are the same observations for the and unit over it. And for this example, it would look something like this, right? You you run it, you would say, okay, you take your data, you you outcome, the treatment column is um the the indicator when it gets first treated. The time column is our year column for this example that we identify on the ID column. And you you see okay we have overall roughly 15,000 observations but the number of unique units is 2500 right because we have the time period so this is the number of unique units in our ID column for for um and then you can use different learners.

### 02:43:01

**Sven Klaassen:** We had this yesterday. So I will skip this one right now also for time reasons. Right? You set up one one regression for your um pro for your trend regression. So the outcome regression and you set up uh one calculation for your your propensity score estimation, right? Just one learner. And the the argument is that uh for you then can use basically we have this multivaried treatment class. So diffid diff over multiper periods for this one which is a wrapper over two lot of two times two settings. So what this internally does it creates a lot of two times two settings and estimates them all of them separately right because different is in principle defined in this very subsets we we are considering like one pre-treatment period one post treatment period right and a diff a corresponding subgroup which we are just taking a look at and so so we have to define what are our regressions for the the um trend propensity score and then which combination which effects we actually want to look at and there are we can take a look in the examples how this this looks like this there are different default configurations.

### 02:44:15

**Sven Klaassen:** So, so this is default configuration says always take the shortest also shortest pre-treatment period just one estimate by by time for all of them. Choose the control group as the units who never got treated. Right? This indicator you say set them the treatment time as either infinity or as a not not a time value for for this one. And how much cross validation do we want to do? And then you call the same fashion fit on the model and it does all the cross fitting and the summary. Yes. Oh, one question.

**Tsz Yan Lam:** Just a question. So um since different uh object can be now into go to the treatment at a different times in the previous page when you say you want to use the control as the one that I never treated does it means that actually you can also say depending on the time that you're interested in looking at your control group is also changing

**Sven Klaassen:** Yeah, that that would be not yet treated, right? We have diff two different control groups and not yet treated changes the control group um at each point in time to the units which did not yet receive treatment.

### 02:45:25

**Sven Klaassen:** But this this then really depends on the two* two setting what what is actually available for this period, right?

**Martin Bierey:** Also just clarification question because in the conceptual part we spoke so long that we need to be careful about common trends and so on but this is handled inside the package now with the new songs function

**Sven Klaassen:** That

**Martin Bierey:** right so if I for example add never treated observations that have a very different trend it would not harm the the effect I'm estimating or do I need to be careful and should I actually

**Sven Klaassen:** is that that is the identification assumption right we we will see the tests or the placebo effects you can see later right what what if if it's estimated but this now the model like the other one is the the the the partially linear models the interactive models they assumed unconfoundedness and estimated your effect even if the unconfoundedness doesn't hold right in the example notebook you'd see like if you added this type of collider you still can run the model. You just get a different effect. You just get a different estimate.

### 02:46:32

**Sven Klaassen:** Here the same thing this the model runs and it assumes parallel trends for the control group right within these different time periods you you you are applying and when when this doesn't hold you still get an estimate. The question is that it might be a bit biased depending on how large this violation actually is. Right? Of course, parlay trends is also usually not it's it's just approximate, right? Like like they would have evolved approximately very similar over time. So I think it's a good plug-in part to estimate your effect or a good ju just to get some some good working model for this. But yeah, you you still have to choose typical choices are standard, right? to say okay you already design your data set you create your data and you say okay in my data I have these units which I think are should be compar comparable based on the features and then I say okay these are the either the never treated and the or the not yet treated okay and then you get a summary for this and you can see it looks quite large for this and the main part is that it now estimates a lot of effects right really every Every row of this is one single two times two setting or one single effect that is estimated.

### 02:47:52

**Sven Klaassen:** So for the one for this one for the ones who got treated in 2004. So the group we have the combination this is a group the pre-treatment period or the pre the the previous evaluation period we say it's set it to 2002 and the period which we are evaluating it the effect is 2003. So this is a placebo test. This is something which already happens before they got treated. Right? They got treated in 2004. But as comparison group, we take this one time difference and see whether the effect should be close to zero. What we are estimating in in this time period for for this one. We you can see it as a graph very shortly after. So, so and but you can see if we are come going then to the evaluation period 2005 we are still using 2003 as a evaluation period because we need to have pre-treatment periods to have the to estimate the trend right so so so after the the the treatment time this stays sort of fixed to the shortest shortest version available so so maybe yeah you can find print this will we also in the the the the the notebook in more detail.

### 02:49:06

**Sven Klaassen:** So if you want to plot the effects, I think it's sometimes a bit more helpful which says okay four different groups for the one who got first treated in 2004 this automatically estimates these five effects. You can see all of them in the table right like but it's sometimes clearer to see. So so the first time period where they got treated is 2004. So afterwards they are colored differently right and before we have all these which is so-called these placebo type tests which should be all if these parallel trends hold in these per periods should be non-significant right of course you have multiple testing problems right if you test a lot of pre-treatment periods right then maybe you need jointly conf jointly valid confidence intervals or things like this but there you can see the in principle these effects should be zero in the pre-treatment periods for all of these settings. And then after the periods, you can see all of these are comparisons of of different time periods. And for example, for for this one, we we can see this is comparing 2006 for this group with a pre-treatment period.

### 02:50:16

**Sven Klaassen:** The first one pre the pre-treatment was is 2003, the closest one, right? So this should actually match this specific line with an estimate of minus 8 point uh minus.08 which I think here would be roughly this one. So, so just to clarify how these effects for all these groups look look like and the same thing for for the first treated into 2005, 2006, 2007 for all these examples. Um, we will go through this one in in more detail in the notebooks. But just before the break, I just wanted to highlight that because this is a lot of effects. What one is usually or what I think is really helpful and usually ve very interesting for these examples are aggregated versions of these effects and the most interesting ones for this one are event study type aggregations. This is the one which I think is used the most for for this one. So this aggregates all the pre-treatment periods and all the post- treatment periods relative to their treatment time. Right? saying okay this is the first time they got treated what is the effect right one period after treatment for all the group was what what was the average effect aggregated to the group size right the average over everybody after these treatment groups and uh in this example there are some maybe some violations with pre-treatment periods but I think overall this still yeah it might be that there's already previously some trend going down right?

### 02:51:59

**Sven Klaassen:** Some downwards trend which which um makes the assumption not as plausible. But I think overall and the question is of course how to evaluate these in these examples. Um whether one can see a negative effect on on these unemployment rates just after the treatment assignment even if the treatment assignment on different states was was in different periods and time period different time periods over this. But this we will do in more detail also in the notebooks for these examples. So just as a very short question uh a very short uh just very shortly are there any open questions else I would say we this was really a really dense part on on the lecture and I I would continue with more specifically with the notebook after after this session. Right. Okay. Um so just for the time um part we would meet again at uh 1:30 right but and and go into two groups right one group will be done by Yan and one by me um just maybe take some time to already because the break is already a bit longer to to already take a look at the notebook try to whether things run so so we can discuss points that are relevant also for you and it's a bit the notebook is already a bit longer but we we can see then in detail what what the questions are. Okay, great. Thanks

_Transcription ended after 03:07:59_

This editable transcript was computer generated and might contain errors. People can also change the text after it was created.
