import streamlit as st

def max_of_three(a, b, c):
    return max(a, max(b, c))

def main():
    st.title("Maximum of Three Numbers")

    num1 = st.number_input("Enter the first number:", step=1)
    num2 = st.number_input("Enter the second number:", step=1)
    num3 = st.number_input("Enter the third number:", step=1)
  
    if st.button("Find Maximum"):
        maximum = max_of_three(num1, num2, num3)
        st.success(f"The maximum of {num1}, {num2}, and {num3} is: {maximum}")

if __name__ == "__main__":
    main()
