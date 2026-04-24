
import pandas as pd, joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
data={"request":["harsha@gmail.com password123","user@gmail.com shopping123","' OR 1=1 --","<script>alert(1)</script>","GET /admin/delete HTTP/1.1"],"label":["genuine","genuine","hacker","hacker","hacker"]}
df=pd.DataFrame(data)
vec=TfidfVectorizer()
X=vec.fit_transform(df["request"])
model=LogisticRegression(max_iter=1000)
model.fit(X,df["label"])
joblib.dump(model,"login_security_model.pkl")
joblib.dump(vec,"vectorizer.pkl")
print("Model created")
