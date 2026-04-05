import streamlit as st
import pandas as pd
books_list=[]
take_book_list=[]
st.title("Book_MAnagement_System")
menu=st.sidebar.selectbox("Choose One",["Home","Add_Book","Take_Book","View_Books"])
if menu == "Home":
    st.write("Welcome to the E-Library Management")
    data = {
        "S.no": [1],
        "Type_Of_Books": [12],
        "Total_Books": [800],
        "Available or Not": ["Available"]
    }
    df = pd.DataFrame(data)
    st.write(df)
elif menu == "Add_Book":
    st.title("You are Adding the Book")
    book_id = st.number_input("Enter Book ID")
    title = st.text_input("Enter Book Title")
    author = st.text_input("Enter Author Name")
    category = st.selectbox("Select Category", ["Programming","Science","History","Fiction"])
    copies = st.number_input("Total Copies",min_value=0)
    year = st.number_input("Publication Year",min_value=0)
    if st.button("Add Book"):
        if book_id == "" or title == "" or author == "" or category == "" or copies == 0 or year == "":
            st.warning('Please Fill all fields')
        else:
            books={
            "book_id":book_id,
            "title":title,
            "author":author,
            "category":category,
            "copies":copies,
            "year":year
            }
            books_list.append(books)
            st.success("Book Added Successfully")
    st.write(book_list)

elif menu == "Take_Book":
    name=st.input("Name")
    book_id=st.number_input("book_id")
    category=st.text_input("Select Category", ["Programming","Science","History","Fiction")
    date = st.date_input("Select Date")
    return_date=st.date_input("Return Date")
    if st.button("Take_Book"):
        if name == "" or book_id == "" or category == "Select Category":
            st.warning("Fill all fields")
        else:
            data={
                "name"=name,
                "book_id"=book_id,
                "category"=category,
                "date"=date
                "Return_Date":return_date
            }
            take_book_list.append(data)
            st.success(f"Book taken by {name} and return book By {return_date}")
            
elif st.button("View_Books"):
    df=pd.DataFrame(book_list)
    st.success("Fetched Successfully")
    if st.button("Take_Book_List"):
        booklist=pd.DataFrame(take_book_list)
    st.success("Fetched Successfully")