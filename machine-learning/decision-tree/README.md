#
## Decision tree
###ID3 
p(xi) means the probability of the event xi occurs

    info(xi) = -log2p(xi)

entropy of information

![entropy formula](./images/entropy.png)

|outlook | temperature | humidity | windy | play |
|--------|------------ |----------| ------|------|
|sunny|hot|high|FALSE|no|
|sunny|hot|high|TRUE|no|
|overcast|hot|high|FALSE|yes|
|rainy|mild|high|FALSE|yes|
|rainy|cool|normal|FALSE|yes|
|rainy|cool|normal|TRUE|no|
|overcast|cool|normal|TRUE|yes|
|sunny|mild|high|FALSE|no|
|sunny|cool|normal|FALSE|yes|
|rainy|mild|normal|FALSE|yes|
|sunny|mild|normal|TRUE|yes|
|overcast|mild|high|TRUE|yes|
|overcast|hot|normal|FALSE|yes|
|rainy|mild|high|TRUE|no|

play: target_attribute

outlook, temperature, humidity, windy: attributes

H(x)= -(5/14*log2(5/14)+9/14*log2(9/14))=0.0940

Take an example of attribute outlook:

|outlook |yes	|no |
|--------|------|--- |
|sunny	 |  2	| 3  |
|overcast|	4   | 0  |
|rainy   |	3   | 2  |

    H(sunny)= -(2/5*log2(2/5)+3/5*log2(3/5)) = 0.971
    H(overcast)=0
    H(rainy)= 0.971
    
    H(outlook|x) = 5/14*0.971 + 0 + 5/14*0.971 = 0.694

Then calculate for each attribute, and take the attribute with min entropy as the feature
 
    max H(feature|X) - H(x)

### C4.5
same principle with ID3, the difference is in the calculation of entropy
In order to compare the value of entropy, C4,5 based on entropy ratio

For each entropy, should multiply a punishment factor (which depends number of category in a feature)

For example a feature with 2 category is better than a feature with 3 category when entropy is same
### Cart

Gini(A) = sum { pi(1-pi) }

Ref:

[ID3] https://www.jianshu.com/p/cf7f605793b1

[ID3 & C4.5] https://www.cnblogs.com/muzixi/p/6566803.html
[Cart] https://zhuanlan.zhihu.com/p/32003259
[cart tree cut] https://www.cnblogs.com/zhangchaoyang/articles/2709922.html