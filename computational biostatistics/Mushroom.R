# Classify data into 'poisonous'(p) and 'edible'(e) from 'class' column

# Put UTSC-Mushroom data into data frame
  # Read in the URL as csv
    CSV <- read.csv("https://tinyurl.com/UTSC-Mushroom", header = TRUE)
  # Define Data as data frame of CSV
    Data <- data.frame(CSV)

# Randomly split data into training (80%) and testing (20%) data sets
  # Load rpart library
    library(rpart)
  # Define ind as sampling through vector of T/F, numbering rows in Data
    ind <- sample(c(T,F), nrow(Data), replace = T, prob = c(0.8, 0.2))
  # Define Training data as Data sliced to include ind
    train.d <- Data[ind,]
  # Define Testing data as Data sliced not to include ind
    test.d <- Data[!ind,]

# Create decision tree for training data with 'class' column acting as DV
  # Create formula (f) by indicating target (class), . = every other column
    f <- class ~ .
  # Make a tree for training data with 3 splits using cp (complexity parameter)
  # cp value was determined by looking at table and graph generated by printcp(Data.tree) & plotcp(Data.tree)
  # printcp showed that a value of 0.01 split twice, so I inferred that cp must be < 0.01
  # plotcp showed that there was an asymptote around 0.01, so then I inserted different values of cp < 0.01
  # through trial and error I found that 0.005 led to 3 splits
    Data.tree <- rpart(f, data= train.d, cp=0.005)
  # Print out the 3 most important features which are used in determining the tree splits
    cat("\n", "------------------------- \n", "The 3 most important features used in determining the tree splits are: \n", "\n")
    print(Data.tree$frame$var)

# Print confusion matrix for test data
  # Define variable testPred as prediction of decision tree based on test data
    testPred <- predict(Data.tree, newdata = test.d, type='class')
  # Check result against testing data
  # True classifications are on rows, predictions are on columns
    cat("\n","------------------------- \n", "Confusion Matrix:", "\n")
    table(testPred, test.d$class)

# Create plot of decision tree
  # Load rpart.plot library
    library(rpart.plot)
  # Save plot as pdf, size of figure 3.375x2, point size = axes thicknes
    pdf(file = "DecisionTree.pdf", 3.375, 2, pointsize = 6)
  # Make plot, cex = font size, font = 2 = bold, main = title
    cat("\n", "------------------------- \n", "Generating Decision Tree Plot... \n", "\n")
    rpart.plot(Data.tree, cex=0.9, font=2, main="Decision Tree")
  # Turn dev off
    dev.off()
