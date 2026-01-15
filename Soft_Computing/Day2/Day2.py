import numpy as np 
import matplotlib.pyplot as plt 
  
# Binary Step Activation Function 
def binary_step(x): 
    return 1 if x >= 0 else 0 
  
# Training Data (OR Function) 
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]]) 
y = np.array([0, 1, 1, 1])
# Initialize weights and bias 
weights = np.zeros(2) 
bias = 0 
learning_rate = 0.1 
converged = False 
iterations = 0 
decision_boundaries = [] 
  
while not converged: 
    iterations += 1 
    previous_weights = weights.copy() 
    previous_bias = bias 
     
    for i in range(len(X)): 
        weighted_sum = np.dot(X[i], weights) + bias 
        prediction = binary_step(weighted_sum) 
        error = y[i] - prediction 
        weights += learning_rate * error * X[i] 
        bias += learning_rate * error 
  
    # Store decision boundary after each epoch 
    if weights[1] != 0: 
        x_vals = np.linspace(-0.5, 1.5, 100) 
        y_vals = -(weights[0] * x_vals + bias) / weights[1] 
        decision_boundaries.append((x_vals, y_vals)) 
        # Check for convergence 
        if np.array_equal(previous_weights, weights) and previous_bias == bias: 
            converged = True 
  
# Plot decision boundary evolution 
plt.figure(figsize=(6, 6)) 
for i, (x_vals, y_vals) in enumerate(decision_boundaries): 
    plt.plot(x_vals, y_vals, label=f'Epoch {i+1}') 
  
# Plot data points 
for i in range(len(X)): 
    plt.scatter(X[i][0], X[i][1], c='red' if y[i] == 0 else 'blue', marker='o', edgecolors='black', s=100) 
  
plt.xlabel('Input 1') 
plt.ylabel('Input 2') 
plt.title('Perceptron Learning with Binary Step Function') 
plt.xlim(-0.5, 1.5) 
plt.ylim(-0.5, 1.5) 
plt.axhline(0, color='black', linewidth=0.5) 
plt.axvline(0, color='black', linewidth=0.5) 
plt.legend() 
plt.grid(True) 
plt.show() 

# Display final weights and number of iterations 
print(f'Final Weights: {weights}') 
print(f'Final Bias: {bias}') 
print(f'Number of Iterations Until Convergence: {iterations}') 