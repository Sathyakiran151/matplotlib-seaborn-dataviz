'''🔹 3️⃣ Sales Data Comparison

Goal: Compare monthly sales of two stores.
Hint:

Create two NumPy arrays (store A, store B).

Find which store performed better each month using np.where(A > B, "A", "B").

Find total and average yearly sales.'''
import numpy as np
# monthly sales in thousands
store_A =np.array([32,12,12,45,34,67,76,45,39,76,65,79])
store_B =np.array([12,45,65,98,65,23,54,62,78,87,76,87])
print("The Monthly sales of Store A:", store_A)
print("The Monthly sales of Store B:", store_B)
print(f"\nThe Higher sales of store A in a Month is : {np.max(store_A)}k Month ({np.argmax(store_A)+1})")
print(f"The Higher sales of store B in a Month is : {np.max(store_B)}k Month ({np.argmax(store_B)+1})")
print(f"\nThe Total sales of store A in a Year is : {np.sum(store_A)}k")
print(f"The Total sales of store B in a Year is : {np.sum(store_B)}k")

print(f"\nThe Average sales of store A is : {np.mean(store_A)}k")
print(f"The Average sales of store B is : {np.mean(store_B,dtype='int')}k")
# Compare monthly performance
better = np.where(store_A > store_B,"store A","store B")
print("\nMonth-wise better performer:", better)
if np.sum(store_A)>np.sum(store_B):
    print("\nOverall Winner is : store_A")
elif np.sum(store_B)>np.sum(store_A):
    print("\nOverall Winner is : store_B")
else:
    print("\n🤝 Both stores performed equally well!")


    