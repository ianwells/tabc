tabc
====

Playing around with TABC tax data.

This data comes from http://www.window.state.tx.us/taxinfo/taxfiles.html

The _small sample files are just taxes from June 2014, for bars that say they are in Houston, downloaded around July 2014.

The _min file is what the js references, and that's tax data from Dec 2014, downloaded January 25 2015.

A bunch more data is in tax.csv, that's about a year's worth of time series data.  The bar index for that is in bars.csv.

Occasionally hosted on http://tabcmap.s3-website-us-east-1.amazonaws.com/

"The Comptroller of Public Accounts cannot vouch for the data or analysis derived from data after it has been retrieved from the Comptroller's Web site."

Lots more Texas civic data at http://www.texastransparency.org/Data_Center/Search_Datasets.php !


Texas only reports taxes paid, but here's their bit about calculating Gross Receipts:

Reported Tax field:

Prior to January 1, 2014, this is Gross Receipts multiplied by 14% (0.14).

To calculate the Gross Receipts (a field not included in this file):
  1. Divide the Reported Tax field by 14
  2. Multiply the results of step 1 by 100
  3. The results of step 2 is the Gross Receipts (plus or minus a 
     small amount from the Reported Tax being rounded).

***Starting January 1, 2014 Reported Tax field:*** 

This is Gross Receipts multiplied by 6.7% (.067).

To calculate the Gross Receipts (a field not included in this file):
  1. Divide the Reported Tax field by 6.7
  2. Multiply the results of step 1 by 100
  3. The results of step 2 is the Gross Receipts (plus or minus a 
     small amount from the Reported Tax being rounded).


IMPORTANT: Many steps are taken to ensure the greatest accuracy
possible for this data. However, some inaccurate data may appear
if the files have not been recently updated.  If you notice 
information that may be incorrect, please notify us so that we can 
take steps to correct the file.

You can reach us at:
  E-mail: open.records@cpa.state.tx.us
  Phone: 1-800-531-5441, ext. 6-6013 (936-6013 in Austin)

ORD Ref-ID: bbs-bev-moly-csv155-np(0107)
