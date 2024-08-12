Tables:

session_sources:

session_id: unique identifier of this session
user_id: user identifier
event_date: date when the session happened
event_time: time when the session happened
channel_name: traffic channel that started this session (e.g. 'Email')
campaign_name: advertising campaign name that started this session (e.g. 'adwords_campaign_123')
campaign_id: campaign identifier that started this session (not all sessions have a campaign_id)
market: regional market that this session belongs to (e.g. 'DE' for Germany)
cpc: cost-per-click of this (this is how much was paid for this session, you can assume its in Euro)
conversions:

conv_id: unique identifier of this conversion
user_id: user identifier
conv_date: date when the conversion happened
market: regional market that this conversion belongs to
revenue: conversion amount (i.e. how much revenue the company earned through this conversion, you can assume its in Euro)
conversions_backend :

conv_id: unique identifier of this conversion
user_id: user identifier
conv_date: date when the conversion happened
market: regional market that this conversion belongs to
revenue: conversion amount
api_adwords_costs :

event_date: date when the AdWords campaign was running
campaign_id: campaign identifier
cost: amount that was spent on running this campaign on this day (assume its in Euro)
clicks: number of times a user clicked on this ad on the given day
attribution_customer_journey :

conv_id: conversion identifier
session_id: session identifier that belonged in the customer journey of the given conv_id
ihc: 'value' of the given session in the given customer journey (1 = 100%)
Note: the sum of 'ihc' column in the 'attribution_customer_journey' should be equal to 1 (100%) for each 'conv_id'

Questions
Are the costs in the 'api_adwords_costs' table fully covered in the 'session_sources' table? Any campaigns where you see issues?
Are the conversions in the 'conversions' table stable over time? Any pattern?
Double check conversions ('conversions' table) with backend ('conversions_backend' table), any issues?
Are attribution results consistent? Do you find any conversions where the 'ihc' values don't make sense?
Do we have an issue with channeling? Are the number of sessions per channel stable over time?
Any other issues?
