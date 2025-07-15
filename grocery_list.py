import streamlit as st

st.title("🛒 Grocery List / To-Do List")

if "Grocery_list" not in st.session_state:
    st.session_state.Grocery_list = []


st.subheader("➕ Add Item")
item = st.text_input("Enter an item:")

if st.button("Add"):
    if item.strip() != "":
        st.session_state.Grocery_list.append(item.strip())
        st.success(f"✅ '{item}' has been added to the list.")
    else:
        st.warning("⚠️ Please enter a valid item.")

st.subheader("📋 View Items")
if st.session_state.Grocery_list:
    for i, itm in enumerate(st.session_state.Grocery_list, start=1):
        st.write(f"{i}. {itm}")
else:
    st.info("🛒 The grocery list is currently empty.")


st.subheader("❌ Remove Item")
if st.session_state.Grocery_list:
    item_to_remove = st.selectbox("Select an item to remove", st.session_state.Grocery_list)

    if st.button("Remove"):
        st.session_state.Grocery_list.remove(item_to_remove)
        st.success(f"❌ '{item_to_remove}' has been removed from the list.")







































'''
Grocery_list=[]
while True:
    print("Grocery List")
    print("1.Add item ")
    print("2.view item")
    print("3.remove item")
    print("4.exit")
    
    choice=int(input("enter number from 1-4 :"))
     
    if choice==1:
        item=input("enter an item : ")
        Grocery_list.append(item)
        print(f'{item} has been added to the list successfully')
    elif choice==2:
        if not Grocery_list:
            print("The list is empty")
        else:
            print("Your Grocery List ")
            for i, item in enumerate(Grocery_list, start=1):
                print(f"{i}. {item}")
    elif choice==3:
        item=input("enter the item to be removed : ")
        if item in Grocery_list:
            Grocery_list.remove(item)
            print(f'{item} is removed from the list')
        else:
            print("Item not found")
    elif choice==4:
        print("GOOD BYEE")
        break
    else:
        print("invalid choice")
     '''