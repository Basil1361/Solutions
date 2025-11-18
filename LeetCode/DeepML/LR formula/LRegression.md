<!-- Linear Regression - Complete Beginner's Guide -->

# 1. Introduction: What is Linear Regression?

## The Basic Idea
Imagine you want to predict the **price of a house** based on its **number of bedrooms**.

### First Attempt (Too Simple):
```
Price = Number of Bedrooms
```
**Problem:** If a house has 3 bedrooms, the price would be $3? That makes no sense!

### Better Attempt (Still Simple):
```
Price = β × Number of Bedrooms
```
Where **β (beta)** is a "weight" or "multiplier"
- Example: If β = $100,000, then 3 bedrooms = $300,000
- **This is called Simple Linear Regression**

**Why it's not perfect:** In reality, data points don't fall on a perfect line - they're scattered around it (scatterplot).

---

# 2. Real World: Multiple Features

## Houses depend on many factors:
- **x₁** = number of bedrooms
- **x₂** = location quality (1-10 scale)
- **x₃** = house age
- **x₄** = square footage
- etc.

## The Formula:
```
y = β₁x₁ + β₂x₂ + β₃x₃ + ... + ε
```

**Where:**
- **y** = actual price (what we observe)
- **β₁, β₂, β₃** = weights (how much each feature matters)
- **x₁, x₂, x₃** = features (bedrooms, location, age, etc.)
- **ε (epsilon)** = error term (random noise we can't predict)

## Matrix Notation (Compact Form):
Instead of writing out every term, we use matrices:

**Model (with error):**
```
y = Xβ + ε
```

**Prediction (our guess, without error):**
```
ŷ = Xβ
```

**Example:**
```
X = [1  3  8]    β = [β₀]    y = [300000]
    [1  4  7]        [β₁]        [400000]
    [1  2  9]        [β₂]        [250000]
    
Column meanings:
- Column 0: bias term (always 1)
- Column 1: number of bedrooms
- Column 2: location quality
```

---

# 3. Main Objective: Minimize Error

## What is a Loss Function?
A **loss function** measures how wrong our predictions are. We want to minimize it!

### Mean Squared Error (MSE) - Most Common:
```
MSE = (1/n) Σᵢ₌₁ⁿ (yᵢ - ŷᵢ)²
```

**Breaking it down:**
- **yᵢ** = actual price of house i
- **ŷᵢ** = our predicted price of house i
- **(yᵢ - ŷᵢ)** = error (how much we're off)
- **(yᵢ - ŷᵢ)²** = squared error (makes all errors positive, punishes big errors more)
- **Σ** = sum over all n houses
- **(1/n)** = average the errors

**Why square the error?**
1. Makes negative errors positive (|-5| and |+5| both become 25)
2. Punishes large errors more (error of 10 is 100, but error of 2 is only 4)
3. Makes the math easier (derivatives are cleaner)

### Mean Absolute Error (MAE) - Alternative:
```
MAE = (1/n) Σᵢ₌₁ⁿ |yᵢ - ŷᵢ|
```
- Just takes absolute value instead of squaring
- Less common because math is harder

### Matrix Form of MSE:
Instead of writing the sum, we can use matrix notation:

```
Loss = (1/2n) Σᵢ₌₁ⁿ (ŷᵢ - yᵢ)²
Loss = (1/2n) (Xβ - y)ᵀ(Xβ - y)
```

**Why (1/2n) instead of (1/n)?**
- The factor of 1/2 makes the derivative cleaner (the 2 will cancel out later)
- It doesn't change where the minimum is, just scales the function

**What does (Xβ - y)ᵀ(Xβ - y) mean?**
- **(Xβ - y)** = vector of all errors [error₁, error₂, ..., errorₙ]
- **ᵀ** means transpose (flip rows to columns)
- **(Xβ - y)ᵀ(Xβ - y)** = dot product = sum of squared errors

---

# 4. Deriving the Best β (The Math Journey!)

## Goal: Find β that minimizes Loss

### Step 1: Expand the Matrix Expression
```
Loss = (1/2n) (Xβ - y)ᵀ(Xβ - y)
```

**Let's expand (Xβ - y)ᵀ(Xβ - y):**
```
(Xβ - y)ᵀ(Xβ - y) = (Xβ)ᵀ(Xβ) - (Xβ)ᵀy - yᵀ(Xβ) + yᵀy
```

**Why? Using FOIL (First, Outer, Inner, Last):**
- **(a - b)(a - b) = a² - ab - ba + b²**
- In matrices: **(Xβ - y)ᵀ(Xβ - y) = (Xβ)ᵀ(Xβ) - (Xβ)ᵀy - yᵀ(Xβ) + yᵀy**

**Simplify (Xβ)ᵀy and yᵀ(Xβ):**
- Both are scalars (single numbers), not matrices
- For scalars: aᵀb = bᵀa
- So: (Xβ)ᵀy = yᵀ(Xβ)
- Therefore: -(Xβ)ᵀy - yᵀ(Xβ) = -2(Xβ)ᵀy = -2yᵀ(Xβ)

**Using matrix property (AB)ᵀ = BᵀAᵀ:**
```
(Xβ)ᵀ(Xβ) = βᵀXᵀXβ
(Xβ)ᵀy = βᵀXᵀy
```

**Final simplified form:**
```
Loss = (1/2n) (βᵀXᵀXβ - 2βᵀXᵀy + yᵀy)
```

---

### Step 2: Take the Derivative with Respect to β

**Goal:** Find where Loss is minimum → Take derivative and set to 0

**Matrix Calculus Rules we need:**
1. **∂(aᵀβ)/∂β = a** (derivative of linear term)
2. **∂(βᵀAβ)/∂β = 2Aβ** (derivative of quadratic term, if A is symmetric)
3. **∂(constant)/∂β = 0** (derivative of constant)

**Apply to our Loss function:**
```
∂Loss/∂β = (1/2n) [∂(βᵀXᵀXβ)/∂β - ∂(2βᵀXᵀy)/∂β + ∂(yᵀy)/∂β]
```

**Term by term:**
1. **∂(βᵀXᵀXβ)/∂β = 2XᵀXβ** (using rule 2, since XᵀX is symmetric)
2. **∂(2βᵀXᵀy)/∂β = 2Xᵀy** (using rule 1)
3. **∂(yᵀy)/∂β = 0** (yᵀy doesn't depend on β)

**Combine:**
```
∂Loss/∂β = (1/2n) (2XᵀXβ - 2Xᵀy)
∂Loss/∂β = (1/n) (XᵀXβ - Xᵀy)
```

**Notice:** The 2 in the denominator (1/2n) cancelled with the 2 from the derivative!

---

### Step 3: Set Derivative to Zero (Find Minimum)

At the minimum, the derivative = 0:
```
(1/n)(XᵀXβ - Xᵀy) = 0
```

**Multiply both sides by n:**
```
XᵀXβ - Xᵀy = 0
```

**Add Xᵀy to both sides:**
```
XᵀXβ = Xᵀy
```

**This is called the "Normal Equation"**

---

### Step 4: Solve for β (The Final Formula!)

**Multiply both sides by (XᵀX)⁻¹:**
```
(XᵀX)⁻¹XᵀXβ = (XᵀX)⁻¹Xᵀy
```

**Since (XᵀX)⁻¹XᵀX = I (identity matrix):**
```
Iβ = (XᵀX)⁻¹Xᵀy
β = (XᵀX)⁻¹Xᵀy
```

## 🎉 THIS IS THE CLOSED-FORM SOLUTION! 🎉

---

# 5. What Does This Mean?

## The Formula: β = (XᵀX)⁻¹Xᵀy

**In plain English:**
- Given training data **X** (features) and **y** (prices)
- We can directly calculate the **best β** that minimizes MSE
- No iteration needed - just matrix operations!

**Components:**
- **Xᵀ** = transpose of X (flip rows and columns)
- **XᵀX** = a square matrix (dimensions: features × features)
- **(XᵀX)⁻¹** = inverse of XᵀX (like division for matrices)
- **Xᵀy** = matrix-vector product

---

# 6. Python Example

```python
import numpy as np

# Sample data: [bias, bedrooms, location]
X = np.array([
    [1, 2, 8],  # House 1: 2 bedrooms, location 8/10
    [1, 3, 7],  # House 2: 3 bedrooms, location 7/10
    [1, 4, 9],  # House 3: 4 bedrooms, location 9/10
    [1, 2, 6]   # House 4: 2 bedrooms, location 6/10
])

y = np.array([200000, 300000, 400000, 180000])  # Actual prices

# Calculate β using the formula: β = (XᵀX)⁻¹Xᵀy
beta = np.linalg.inv(X.T @ X) @ X.T @ y

print(f"β = {beta}")
# Example output: β = [50000, 80000, 5000]
# Meaning:
#   - Base price: $50,000
#   - Each bedroom adds: $80,000
#   - Each location point adds: $5,000

# Make a prediction for a new house: 3 bedrooms, location 8
new_house = np.array([1, 3, 8])
predicted_price = new_house @ beta
print(f"Predicted price: ${predicted_price:,.0f}")
```

---