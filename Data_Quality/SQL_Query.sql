-- This query outputs a report on campaign_name, total_adwords_cost, total_session_cpc & the discrepancy between the two tables' costs. Running each section of the query will allow for more in dept analysis and finding issues’ root causes.
SELECT 
CAMPAIGN_NAME,
ROUND(SUM(TOTAL_ADWORDS_COST), 2) AS "TOTAL_ADWORDS_COST",
ROUND(SUM(TOTAL_SESSION_CPC), 2) AS "TOTAL_SESSION_CPC",
ROUND(SUM(DIFF), 2) AS "DISCREPANCY"

FROM
-- This section outputs costs and CPC from API & session table, grouped by event_date & campaign_date
(SELECT 
A.EVENT_DATE, 
A.CAMPAIGN_ID, 
A.TOTAL_ADWORDS_COST, 
S.TOTAL_SESSION_CPC, 
(A.TOTAL_ADWORDS_COST - S.TOTAL_SESSION_CPC) AS "DIFF", 
S.CAMPAIGN_NAME

FROM
-- This section summarises costs from api_adwords_cost
(SELECT 
EVENT_DATE, 
CAMPAIGN_ID, 
SUM(COST) AS TOTAL_ADWORDS_COST 

FROM API_ADWORDS_COSTS 
GROUP BY EVENT_DATE, CAMPAIGN_ID) A

LEFT JOIN 
-- This section summarises CPC in session_sources
(SELECT 
EVENT_DATE, 
CAMPAIGN_ID, 
CAMPAIGN_NAME, 
SUM(CPC) AS TOTAL_SESSION_CPC 

FROM SESSION_SOURCES 
GROUP BY EVENT_DATE, CAMPAIGN_ID) S

ON A.EVENT_DATE = S.EVENT_DATE AND A.CAMPAIGN_ID = S.CAMPAIGN_ID)

WHERE DIFF <> 0 
GROUP BY CAMPAIGN_NAME
ORDER BY DIFF DESC

