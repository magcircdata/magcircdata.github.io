# from scrapy.http import HtmlResponse
from lxml import html
import requests
import pandas as pd

#http://stackoverflow.com/questions/28305578/python-get-html-table-data-by-xpath

page = requests.get('https://en.wikipedia.org/wiki/List_of_U.S._states_by_historical_population')
tree = html.fromstring("""<table class="wikitable sortable jquery-tablesorter" style="text-align:right;">
<thead><tr>
<th class="headerSort" tabindex="0" role="columnheader button" title="Sort ascending">Name</th>
<th class="headerSort" tabindex="0" role="columnheader button" title="Sort ascending">1870</th>
<th class="headerSort" tabindex="0" role="columnheader button" title="Sort ascending">1880</th>
<th class="headerSort" tabindex="0" role="columnheader button" title="Sort ascending">1890</th>
<th class="headerSort" tabindex="0" role="columnheader button" title="Sort ascending">1900</th>
<th class="headerSort" tabindex="0" role="columnheader button" title="Sort ascending">1910</th>
<th class="headerSort" tabindex="0" role="columnheader button" title="Sort ascending">1920</th>
<th class="headerSort" tabindex="0" role="columnheader button" title="Sort ascending">1930</th>
<th class="headerSort" tabindex="0" role="columnheader button" title="Sort ascending">1940</th>
<th class="headerSort" tabindex="0" role="columnheader button" title="Sort ascending">1950</th>
</tr></thead><tbody>
<tr>
<td style="font-weight:bold" height="13" align="left">Alabama</td>
<td>996,992</td>
<td>1,262,505</td>
<td>1,513,017</td>
<td>1,828,697</td>
<td>2,138,093</td>
<td>2,348,174</td>
<td>2,646,248</td>
<td>2,832,961</td>
<td>3,061,743</td>
</tr>
<tr>
<td style="font-weight:bold" height="13" align="left">Alaska</td>
<td style="background-color:#D8D8D8">&nbsp;</td>
<td style="background-color:#D8D8D8">&nbsp;</td>
<td style="background-color:#D8D8D8">33,426</td>
<td style="background-color:#D8D8D8">32,052</td>
<td style="background-color:#D8D8D8">64,356</td>
<td style="background-color:#D8D8D8">55,036</td>
<td style="background-color:#D8D8D8">59,278</td>
<td style="background-color:#D8D8D8">72,524</td>
<td style="background-color:#D8D8D8">128,643</td>
</tr>
<tr>
<td style="font-weight:bold" height="13" align="left">Arizona</td>
<td style="background-color:#D8D8D8">9,658</td>
<td style="background-color:#D8D8D8">40,440</td>
<td style="background-color:#D8D8D8">88,243</td>
<td style="background-color:#D8D8D8">122,931</td>
<td style="background-color:#D8D8D8">204,354</td>
<td>334,162</td>
<td>435,573</td>
<td>499,261</td>
<td>749,587</td>
</tr>
<tr>
<td style="font-weight:bold" height="13" align="left">Arkansas</td>
<td>484,471</td>
<td>802,525</td>
<td>1,128,211</td>
<td>1,311,564</td>
<td>1,574,449</td>
<td>1,752,204</td>
<td>1,854,482</td>
<td>1,949,387</td>
<td>1,909,511</td>
</tr>
<tr>
<td style="font-weight:bold" height="13" align="left">California</td>
<td>560,247</td>
<td>864,694</td>
<td>1,213,398</td>
<td>1,485,053</td>
<td>2,377,549</td>
<td>3,426,861</td>
<td>5,677,251</td>
<td>6,907,387</td>
<td>10,586,223</td>
</tr>
<tr>
<td style="font-weight:bold" height="13" align="left">Colorado</td>
<td style="background-color:#D8D8D8">39,864</td>
<td>194,327</td>
<td>413,249</td>
<td>539,700</td>
<td>799,024</td>
<td>939,629</td>
<td>1,035,791</td>
<td>1,123,296</td>
<td>1,325,089</td>
</tr>
<tr>
<td style="font-weight:bold" height="13" align="left">Connecticut</td>
<td>537,454</td>
<td>622,700</td>
<td>746,258</td>
<td>908,420</td>
<td>1,114,756</td>
<td>1,380,631</td>
<td>1,606,903</td>
<td>1,709,242</td>
<td>2,007,280</td>
</tr>
<tr>
<td style="font-weight:bold" height="13" align="left">Delaware</td>
<td>125,015</td>
<td>146,608</td>
<td>168,493</td>
<td>184,735</td>
<td>202,322</td>
<td>223,003</td>
<td>238,380</td>
<td>266,505</td>
<td>318,085</td>
</tr>
<tr>
<td height="13" align="left"><b>District&nbsp;of&nbsp;Columbia</b></td>
<td>131,700</td>
<td>177,624</td>
<td>230,392</td>
<td>278,718</td>
<td>331,069</td>
<td>437,571</td>
<td>486,869</td>
<td>663,091</td>
<td>802,178</td>
</tr>
<tr>
<td style="font-weight:bold" height="13" align="left">Florida</td>
<td>187,748</td>
<td>269,493</td>
<td>391,422</td>
<td>528,542</td>
<td>752,619</td>
<td>968,470</td>
<td>1,468,211</td>
<td>1,897,414</td>
<td>2,771,305</td>
</tr>
<tr>
<td style="font-weight:bold" height="13" align="left">Georgia</td>
<td>1,184,109</td>
<td>1,542,180</td>
<td>1,837,353</td>
<td>2,216,331</td>
<td>2,609,121</td>
<td>2,895,832</td>
<td>2,908,506</td>
<td>3,123,723</td>
<td>3,444,578</td>
</tr>
<tr>
<td style="font-weight:bold" height="13" align="left">Hawaii</td>
<td style="background-color:#D8D8D8">&nbsp;</td>
<td style="background-color:#D8D8D8">&nbsp;</td>
<td style="background-color:#D8D8D8">&nbsp;</td>
<td style="background-color:#D8D8D8">154,001</td>
<td style="background-color:#D8D8D8">191,909</td>
<td style="background-color:#D8D8D8">255,912</td>
<td style="background-color:#D8D8D8">368,336</td>
<td style="background-color:#D8D8D8">423,330</td>
<td style="background-color:#D8D8D8">499,794</td>
</tr>
<tr>
<td style="font-weight:bold" height="13" align="left">Idaho</td>
<td style="background-color:#D8D8D8">14,999</td>
<td style="background-color:#D8D8D8">32,610</td>
<td>88,548</td>
<td>161,772</td>
<td>325,594</td>
<td>431,866</td>
<td>445,032</td>
<td>524,873</td>
<td>588,637</td>
</tr>
<tr>
<td style="font-weight:bold" height="13" align="left">Illinois</td>
<td>2,539,891</td>
<td>3,077,871</td>
<td>3,826,351</td>
<td>4,821,550</td>
<td>5,638,591</td>
<td>6,485,280</td>
<td>7,630,654</td>
<td>7,897,241</td>
<td>8,712,176</td>
</tr>
<tr>
<td style="font-weight:bold" height="13" align="left">Indiana</td>
<td>1,680,637</td>
<td>1,978,301</td>
<td>2,192,404</td>
<td>2,516,462</td>
<td>2,700,876</td>
<td>2,930,390</td>
<td>3,238,503</td>
<td>3,427,796</td>
<td>3,934,224</td>
</tr>
<tr>
<td style="font-weight:bold" height="13" align="left">Iowa</td>
<td>1,194,020</td>
<td>1,624,615</td>
<td>1,912,297</td>
<td>2,231,853</td>
<td>2,224,771</td>
<td>2,404,021</td>
<td>2,470,939</td>
<td>2,538,268</td>
<td>2,621,073</td>
</tr>
<tr>
<td style="font-weight:bold" height="13" align="left">Kansas</td>
<td>364,399</td>
<td>996,096</td>
<td>1,428,108</td>
<td>1,470,495</td>
<td>1,690,949</td>
<td>1,769,257</td>
<td>1,880,999</td>
<td>1,801,028</td>
<td>1,905,299</td>
</tr>
<tr>
<td style="font-weight:bold" height="13" align="left">Kentucky</td>
<td>1,321,011</td>
<td>1,648,690</td>
<td>1,858,635</td>
<td>2,147,174</td>
<td>2,289,905</td>
<td>2,416,630</td>
<td>2,614,589</td>
<td>2,845,627</td>
<td>2,944,806</td>
</tr>
<tr>
<td style="font-weight:bold" height="13" align="left">Louisiana</td>
<td>726,915</td>
<td>939,946</td>
<td>1,118,587</td>
<td>1,381,625</td>
<td>1,656,388</td>
<td>1,798,509</td>
<td>2,101,593</td>
<td>2,363,880</td>
<td>2,683,516</td>
</tr>
<tr>
<td style="font-weight:bold" height="13" align="left">Maine</td>
<td>626,915</td>
<td>648,936</td>
<td>661,086</td>
<td>694,466</td>
<td>742,371</td>
<td>768,014</td>
<td>797,423</td>
<td>847,226</td>
<td>913,774</td>
</tr>
<tr>
<td style="font-weight:bold" height="13" align="left">Maryland</td>
<td>780,894</td>
<td>934,943</td>
<td>1,042,390</td>
<td>1,188,044</td>
<td>1,295,346</td>
<td>1,449,661</td>
<td>1,631,526</td>
<td>1,821,244</td>
<td>2,343,001</td>
</tr>
<tr>
<td style="font-weight:bold" height="13" align="left">Massachusetts</td>
<td>1,457,351</td>
<td>1,783,085</td>
<td>2,238,943</td>
<td>2,805,346</td>
<td>3,366,416</td>
<td>3,852,356</td>
<td>4,249,614</td>
<td>4,316,721</td>
<td>4,690,514</td>
</tr>
<tr>
<td style="font-weight:bold" height="13" align="left">Michigan</td>
<td>1,184,059</td>
<td>1,636,937</td>
<td>2,093,889</td>
<td>2,420,982</td>
<td>2,810,173</td>
<td>3,668,412</td>
<td>4,842,325</td>
<td>5,256,106</td>
<td>6,371,766</td>
</tr>
<tr>
<td style="font-weight:bold" height="13" align="left">Minnesota</td>
<td>439,706</td>
<td>780,773</td>
<td>1,310,283</td>
<td>1,751,394</td>
<td>2,075,708</td>
<td>2,387,125</td>
<td>2,563,953</td>
<td>2,792,300</td>
<td>2,982,483</td>
</tr>
<tr>
<td style="font-weight:bold" height="13" align="left">Mississippi</td>
<td>827,922</td>
<td>1,131,597</td>
<td>1,289,600</td>
<td>1,551,270</td>
<td>1,797,114</td>
<td>1,790,618</td>
<td>2,009,821</td>
<td>2,183,796</td>
<td>2,178,914</td>
</tr>
<tr>
<td style="font-weight:bold" height="13" align="left">Missouri</td>
<td>1,721,295</td>
<td>2,168,380</td>
<td>2,679,184</td>
<td>3,106,665</td>
<td>3,293,335</td>
<td>3,404,055</td>
<td>3,629,367</td>
<td>3,784,664</td>
<td>3,954,653</td>
</tr>
<tr>
<td style="font-weight:bold" height="13" align="left">Montana</td>
<td style="background-color:#D8D8D8">20,595</td>
<td style="background-color:#D8D8D8">39,159</td>
<td>142,924</td>
<td>243,329</td>
<td>376,053</td>
<td>548,889</td>
<td>537,606</td>
<td>559,456</td>
<td>591,024</td>
</tr>
<tr>
<td style="font-weight:bold" height="13" align="left">Nebraska</td>
<td>122,993</td>
<td>452,402</td>
<td>1,062,656</td>
<td>1,066,300</td>
<td>1,192,214</td>
<td>1,296,372</td>
<td>1,377,963</td>
<td>1,315,834</td>
<td>1,325,510</td>
</tr>
<tr>
<td style="font-weight:bold" height="13" align="left">Nevada</td>
<td>42,491</td>
<td>62,266</td>
<td>47,355</td>
<td>42,335</td>
<td>81,875</td>
<td>77,407</td>
<td>91,058</td>
<td>110,247</td>
<td>160,083</td>
</tr>
<tr>
<td style="font-weight:bold" height="13" align="left">New Hampshire</td>
<td>318,300</td>
<td>346,991</td>
<td>376,530</td>
<td>411,588</td>
<td>430,572</td>
<td>443,083</td>
<td>465,293</td>
<td>491,524</td>
<td>533,242</td>
</tr>
<tr>
<td style="font-weight:bold" height="13" align="left">New Jersey</td>
<td>906,096</td>
<td>1,131,116</td>
<td>1,444,933</td>
<td>1,883,669</td>
<td>2,537,167</td>
<td>3,155,900</td>
<td>4,041,334</td>
<td>4,160,165</td>
<td>4,835,329</td>
</tr>
<tr>
<td style="font-weight:bold" height="13" align="left">New Mexico</td>
<td style="background-color:#D8D8D8">91,874</td>
<td style="background-color:#D8D8D8">119,565</td>
<td style="background-color:#D8D8D8">160,282</td>
<td style="background-color:#D8D8D8">195,310</td>
<td style="background-color:#D8D8D8">327,301</td>
<td>360,350</td>
<td>423,317</td>
<td>531,818</td>
<td>681,187</td>
</tr>
<tr>
<td style="font-weight:bold" height="13" align="left">New York</td>
<td>4,382,759</td>
<td>5,082,871</td>
<td>6,003,174</td>
<td>7,268,894</td>
<td>9,113,614</td>
<td>10,385,227</td>
<td>12,588,066</td>
<td>13,479,142</td>
<td>14,830,192</td>
</tr>
<tr>
<td style="font-weight:bold" height="13" align="left">North Carolina</td>
<td>1,071,361</td>
<td>1,399,750</td>
<td>1,617,947</td>
<td>1,893,810</td>
<td>2,206,287</td>
<td>2,559,123</td>
<td>3,170,276</td>
<td>3,571,623</td>
<td>4,061,929</td>
</tr>
<tr>
<td style="font-weight:bold" height="13" align="left">North Dakota</td>
<td style="background-color:#D8D8D8">2,405</td>
<td style="background-color:#D8D8D8">36,909</td>
<td>190,983</td>
<td>319,146</td>
<td>577,056</td>
<td>646,872</td>
<td>680,845</td>
<td>641,935</td>
<td>619,636</td>
</tr>
<tr>
<td style="font-weight:bold" height="13" align="left">Ohio</td>
<td>2,665,260</td>
<td>3,198,062</td>
<td>3,672,316</td>
<td>4,157,545</td>
<td>4,767,121</td>
<td>5,759,394</td>
<td>6,646,697</td>
<td>6,907,612</td>
<td>7,946,627</td>
</tr>
<tr>
<td style="font-weight:bold" height="13" align="left">Oklahoma</td>
<td style="background-color:#D8D8D8">&nbsp;</td>
<td style="background-color:#D8D8D8">&nbsp;</td>
<td style="background-color:#D8D8D8">258,657</td>
<td style="background-color:#D8D8D8">790,391</td>
<td>1,657,155</td>
<td>2,028,283</td>
<td>2,396,040</td>
<td>2,336,434</td>
<td>2,233,351</td>
</tr>
<tr>
<td style="font-weight:bold" height="13" align="left">Oregon</td>
<td>90,923</td>
<td>174,768</td>
<td>317,704</td>
<td>413,536</td>
<td>672,765</td>
<td>783,389</td>
<td>953,786</td>
<td>1,089,684</td>
<td>1,521,341</td>
</tr>
<tr>
<td style="font-weight:bold" height="13" align="left">Pennsylvania</td>
<td>3,521,951</td>
<td>4,282,891</td>
<td>5,258,014</td>
<td>6,302,115</td>
<td>7,665,111</td>
<td>8,720,017</td>
<td>9,631,350</td>
<td>9,900,180</td>
<td>10,498,012</td>
</tr>
<tr>
<td style="font-weight:bold" height="13" align="left">Rhode Island</td>
<td>217,353</td>
<td>276,531</td>
<td>345,506</td>
<td>428,556</td>
<td>542,610</td>
<td>604,397</td>
<td>687,497</td>
<td>713,346</td>
<td>791,896</td>
</tr>
<tr>
<td style="font-weight:bold" height="13" align="left">South Carolina</td>
<td>705,606</td>
<td>995,577</td>
<td>1,151,149</td>
<td>1,340,316</td>
<td>1,515,400</td>
<td>1,683,724</td>
<td>1,738,765</td>
<td>1,899,804</td>
<td>2,117,027</td>
</tr>
<tr>
<td style="font-weight:bold" height="13" align="left">South Dakota</td>
<td style="background-color:#D8D8D8">11,776</td>
<td style="background-color:#D8D8D8">98,268</td>
<td>348,600</td>
<td>401,570</td>
<td>583,888</td>
<td>636,547</td>
<td>692,849</td>
<td>642,961</td>
<td>652,740</td>
</tr>
<tr>
<td style="font-weight:bold" height="13" align="left">Tennessee</td>
<td>1,258,520</td>
<td>1,542,359</td>
<td>1,767,518</td>
<td>2,020,616</td>
<td>2,184,789</td>
<td>2,337,885</td>
<td>2,616,556</td>
<td>2,915,841</td>
<td>3,291,718</td>
</tr>
<tr>
<td style="font-weight:bold" height="13" align="left">Texas</td>
<td>818,579</td>
<td>1,591,749</td>
<td>2,235,523</td>
<td>3,048,710</td>
<td>3,896,542</td>
<td>4,663,228</td>
<td>5,824,715</td>
<td>6,414,824</td>
<td>7,711,194</td>
</tr>
<tr>
<td style="font-weight:bold" height="13" align="left">Utah</td>
<td style="background-color:#D8D8D8">86,336</td>
<td style="background-color:#D8D8D8">143,963</td>
<td style="background-color:#D8D8D8">210,779</td>
<td>276,749</td>
<td>373,351</td>
<td>449,396</td>
<td>507,847</td>
<td>550,310</td>
<td>688,862</td>
</tr>
<tr>
<td style="font-weight:bold" height="13" align="left">Vermont</td>
<td>330,551</td>
<td>332,286</td>
<td>332,422</td>
<td>343,641</td>
<td>355,956</td>
<td>352,428</td>
<td>359,611</td>
<td>359,231</td>
<td>377,747</td>
</tr>
<tr>
<td style="font-weight:bold" height="13" align="left">Virginia</td>
<td>1,225,163</td>
<td>1,512,565</td>
<td>1,655,980</td>
<td>1,854,184</td>
<td>2,061,612</td>
<td>2,309,187</td>
<td>2,421,851</td>
<td>2,677,773</td>
<td>3,318,680</td>
</tr>
<tr>
<td style="font-weight:bold" height="13" align="left">Washington</td>
<td style="background-color:#D8D8D8">23,955</td>
<td style="background-color:#D8D8D8">75,116</td>
<td>357,232</td>
<td>518,103</td>
<td>1,141,990</td>
<td>1,356,621</td>
<td>1,563,396</td>
<td>1,736,191</td>
<td>2,378,963</td>
</tr>
<tr>
<td style="font-weight:bold" height="13" align="left">West Virginia</td>
<td>442,014</td>
<td>618,457</td>
<td>762,794</td>
<td>958,800</td>
<td>1,221,119</td>
<td>1,463,701</td>
<td>1,729,205</td>
<td>1,901,974</td>
<td>2,005,552</td>
</tr>
<tr>
<td style="font-weight:bold" height="13" align="left">Wisconsin</td>
<td>1,054,670</td>
<td>1,315,497</td>
<td>1,693,330</td>
<td>2,069,042</td>
<td>2,333,860</td>
<td>2,632,067</td>
<td>2,939,006</td>
<td>3,137,587</td>
<td>3,434,575</td>
</tr>
<tr>
<td style="font-weight:bold" height="13" align="left">Wyoming</td>
<td style="background-color:#D8D8D8">9,118</td>
<td style="background-color:#D8D8D8">20,789</td>
<td>60,705</td>
<td>92,531</td>
<td>145,965</td>
<td>194,402</td>
<td>225,565</td>
<td>250,742</td>
<td>290,529</td>
</tr>
<tr class="sortbottom" bgcolor="#B2BEB5">
<td style="font-weight:bold" height="13" align="left"><b>United States</b></td>
<td>38,558,371</td>
<td>50,155,783</td>
<td>62,947,714<sup id="cite_ref-11" class="reference"><a href="#cite_note-11" wotsearchprocessed="true">[11]</a></sup></td>
<td>75,994,575</td>
<td>91,972,266</td>
<td>105,710,620</td>
<td>122,775,046</td>
<td>131,669,275</td>
<td>150,697,361</td>
</tr>
</tbody><tfoot></tfoot></table>""")
# print page.content
table = tree.xpath('//table')[0]

headers = [th.text_content().replace(u'\xa0', u' ') for th in table.xpath('//th')]

data = [[td.text_content().replace(u'\xa0', u' ') for td in tr.xpath('td')] for tr in table.xpath('//tr')][2:]

pd.DataFrame(data, columns=headers).to_csv("census_data.csv", index=False)