## SQL Challenge:


I was working on a project which utilized the Markov chain. I had an interesting time solving a matrix manipulation problem. I thought I should share the problem here. 

## Context:
I am using Markov transition probabilities as a feature matrix for a machine learning algorithm but the problem is for a single document D it will create R rows for each state S R = D x S  whereas the feature matrix should contain 1 R per D. So, the goal is to convert this R = D (1 row for 1 document) 


Given the transition matrix of a Markov chain represented as a table in an SQL database. Each row in the table represents the probability of transitioning from one state to another.
Please refer to Fig. 1 for a sample input format.

<img width="355" alt="fig 1  input format" src="https://github.com/DanielOX/markov-chain-problem/assets/33195456/f88d380b-a1a2-418c-bf85-dc4b9acace07">



Each row represents the transition probabilities from a previous state (val) to a current state (a, b, c). 


so it's important to note that a -> b is not equal to b -> a because the probability of change in the state of event a to state b would be different from the probability of change in the state of event b to a


## Problem Statement: 

Write a SQL query to generate all possible state combinations (e.g., a_a, a_b, a_c, b_a, b_b, b_c, c_a, c_b, c_c) along with their corresponding transition probabilities.


### Input:


You are provided with a table named transition matrix having the following schema:


   prev_state: Represents the previous state (can be a, b, or c).

   a: Probability of transitioning to state a from the previous state.

   b: Probability of transitioning to state b from the previous state.

   c: Probability of transitioning to state c from the previous state.


### Output


The output should contain a single row representing all possible state combinations, where each state combination (e.g., a_a, a_b, a_c, b_a, b_b, b_c, c_a, c_b, c_c) serves as a column name. The corresponding cell values in this row should be the probabilities of transitioning between the states. 


<img width="587" alt="fig 2  output format" src="https://github.com/DanielOX/markov-chain-problem/assets/33195456/73211017-33b1-48bd-a5e1-7fd46e8bab06">


### Constraints: 

1. Each state (a, b, c) can transition to any other state (a, b, c) based on the given probabilities.

2. Probabilities are represented as decimal numbers between 0 and 1.

3. Each state combination must appear as a column in the output even if the transition probability is 0.


### Hint: 

You can use conditional aggregation (e.g., CASE statements within aggregate functions like MAX() or MIN()) to pivot the data and generate the desired output format. A dummy monotonically increasing column needs to be added.




