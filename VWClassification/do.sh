
# to build model
cat train.txt | python ./trainset2vw.py | vw --loss_function logistic --passes 20 --cache_file .cache --l2 0.00000001 --l1 0.00000001 -q ll --ngram 2 --nn 10 -b 24 -f finalmodel2.vw

# to predict
cat test.txt | python ./testset2vw.py | vw -t -i finalmodel2.vw -p pred.txt

# to compile java kagglefyer
javac Kagglefy.java

# to kagglefy pred.txt
java Kagglefy

# a file named "kaggle.out" will be produced

echo "the file kaggle.out can now be submitted to Kaggle for scoring"
