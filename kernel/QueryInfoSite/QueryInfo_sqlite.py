from kernel.QueryInfoSite.DataLoader import sql, data_path, quote
from kernel.QueryInfoSite.ExceptionClasses_Query import *
import pandas as pd


def Query_UserRentingHis(user_id):
    with sql.connect(data_path) as conn:
        try:
            cursor = conn.execute("""
                    select Book.BookId, Book.BookName, BookType.TypeName, RentHistory.RentDay, RentHistory.ReturnDate
                    from User, Book, RentHistory, BookType
                    where User.UserId = %s and BookType.TypeId = Book.Type
                    and User.UserId = RentHistory.UserId and Book.BookId = RentHistory.BookId
                """ % (quote(user_id)))
        except sql.DatabaseError as e:
            # 先放这个，不能没有显示
            cursor = None
            print(repr(e))
            pass
        if cursor is not None:
            res = cursor.fetchall()
    return res


def Query_BookRank():
    with sql.connect(data_path) as conn:
        try:
            cursor = conn.execute("""
                select Book.BookId, BookName, times, Stock, Price, TypeName from Book, BookType,
                (
                select BookId, count(*) as times from RentHistory
                group by BookId
                ) as temp
                where Book.BookId = temp.BookId and Book.Type = BookType.TypeId
                order by times desc""")
        except sql.DatabaseError as e:
            # 先放这个，不能没有显示
            cursor = None
            print(repr(e))
            pass
        if cursor is not None:
            res = cursor.fetchall()
    return res


def Query_UserRank():
    with sql.connect(data_path) as conn:
        try:
            cursor = conn.execute("""
                select UserName, User.UserId, times from User, 
                (
                select UserId, count(*) as times from RentHistory
                group by UserId
                )as temp
                where User.UserId = temp.UserId
                order by times desc""")
        except sql.DatabaseError as e:
            # 先放这个，不能没有显示
            cursor = None
            print(repr(e))
            pass
        if cursor is not None:
            res = cursor.fetchall()
    return res


def Query_BookType():
    with sql.connect(data_path) as conn:
        try:
            cursor = conn.execute("""
                select * from BookType
                """)
        except sql.DatabaseError as e:
            # 先放这个，不能没有显示
            cursor = None
            print(repr(e))
            pass
        if cursor is not None:
            res = cursor.fetchall()
    return res


def Query_BookType_Id():
    with sql.connect(data_path) as conn:
        try:
            cursor = conn.execute("""
                select TypeId
                from BookType
                """)
        except sql.DatabaseError as e:
            # 先放这个，不能没有显示
            cursor = None
            print(repr(e))
            pass
        if cursor is not None:
            res = cursor.fetchall()
    return res


def Query_Book(TypeName, BookInfo):
    res = None
    with sql.connect(data_path) as conn:
        try:
            cursor = conn.execute("""
                select Book.BookName, Book.BookId
                from Book, BookType
                where Book.Type = BookType.TypeId and BookType.TypeName = {0}
                and Book.BookName like '%{1}%' and Book.Stock > 0
                """.format(quote(TypeName), BookInfo))
        except sql.DatabaseError as e:
            # 先放这个，不能没有显示
            cursor = None
            print("Query Fail", repr(e))
            pass
        if cursor is not None:
            res = cursor.fetchall()
    return res


def Query_UnReturned_Book(UserId):
    res = None
    with sql.connect(data_path) as conn:
        try:
            cursor = conn.execute("""
                select User.UserId, User.UserName, RentHistory.BookId, Book.BookName, 
                RentHistory.RentDay
                from
                RentHistory, User, Book
                where 
                User.UserId = RentHistory.UserId
                and Book.BookId = RentHistory.BookId
                and RentHistory.ReturnDate is null 
                and User.UserId is '{}'
                """.format(str(UserId)))
        except sql.DatabaseError as e:
            # 先放这个，不能没有显示
            cursor = None
            print("Query Fail", repr(e))
            pass
        if cursor is not None:
            res = cursor.fetchall()
    return res


def Query_Price_Remain(UserId, BookId=None, RentDate=None):

    req = """
        select * from UnreturnPrice
        where UserId = {}
        """.format(str(UserId))

    if BookId is not None:
        req += " and BookId = {}".format(str(BookId))

    if RentDate is not None:
        req += " and RentDay = {}".format(str(RentDate))

    res = None
    with sql.connect(data_path) as conn:
        try:
            cursor = conn.execute(req)
        except sql.DatabaseError as e:
            # 先放这个，不能没有显示
            cursor = None
            print("Query Fail", repr(e))
            pass
        if cursor is not None:
            res = cursor.fetchall()
    return res


def Modify_Return(tar):
    if len(tar) != 3:
        return
    UserId, BookId, RentDate = tar
    with sql.connect(data_path) as conn:
        conn.execute("""
        update RentHistory
        set ReturnDate = date('now')
        where UserId = '{}'
        and BookId = '{}'
        and RentDay = '{}'
        and ReturnDate is null
        """.format(str(UserId), str(BookId), RentDate))
    pass


def RentCertification(UserId, BookId) -> bool:
    with sql.connect(data_path) as conn:
        cursor = conn.execute("""
            select * from UserUnReturn_Count
            where UserId = '{}'
        """.format(str(UserId)))
        tar = cursor.fetchall()
        if len(tar) == 0:
            pass
        else:
            if tar[0][1] >= tar[0][2]:
                raise RentRefuse()
    with sql.connect(data_path) as conn:
        cursor = conn.execute("""
            select * from BookRemain
            where BookId = '{}'
        """.format(str(BookId)))
        tar = cursor.fetchall()
        if len(tar) == 0:
            pass
        else:
            if tar[0][1] <= 0:
                raise RentRefuse()
    return True


def Add_RentHis(UserId, BookId):
    RentCertification(UserId, BookId)
    with sql.connect(data_path) as conn:
        conn.execute("""
            insert into RentHistory
            values
            ({0},{1},date('now'),null)
            """.format(quote(UserId), quote(BookId)))
    pass


def Add_Book(BookId, BookName, stock, price, BookType):
    with sql.connect(data_path) as conn:
        conn.execute("""
        insert into Book
        values(
        '{}', '{}', {}, {}, '{}'
        )
        """.format(str(BookId), str(BookName), stock, price, str(BookType)))
    pass


def Add_BookType(Id, Name):
    with sql.connect(data_path) as conn:
        conn.execute("""
        insert into BookType
        values(
        '{}', '{}'
        )
        """.format(str(Id), str(Name)))
    pass


def Add_User(UserId, UserName, Role, Password):
    with sql.connect(data_path) as conn:
        conn.execute("""
                insert into User
                values
                (%s,%s,%d,%s)
            """ % (quote(UserId), UserName, Role, quote(Password)))


def Update_UserInfo(pack):
    try:
        with sql.connect(data_path) as conn:
            conn.execute("""
                update User set UserName = '{}',
                Password = '{}',
                Role = '{}'
                where UserId = '{}' 
                """.format(pack['name'], pack['password'], pack['role'], pack['id']))
    except Exception as e:
        raise RentRefuse(repr(e))
    pass


def Update_BookInfo(pack):
    try:
        with sql.connect(data_path) as conn:
            conn.execute("""
                update Book set BookName = '{}',
                Stock = '{}',
                Price = '{}',
                Type = ''
                where UserId = '{}' 
                """.format(pack['name'], pack['Stock'], pack['price'], pack['type id'], pack['id']))
    except Exception as e:
        raise RentRefuse(repr(e))
    pass


def FetchAllBooks():
    res = None
    with sql.connect(data_path) as conn:
        try:
            cursor = conn.execute("""
            select * from Book
            """)
        except sql.DatabaseError as e:
            # 先放这个，不能没有显示
            cursor = None
            print("Query Fail", repr(e))
            pass
        if cursor is not None:
            res = cursor.fetchall()
    return res


def FetchAllBookType():
    res = None
    with sql.connect(data_path) as conn:
        try:
            cursor = conn.execute("""
            select * from BookType
            """)
        except sql.DatabaseError as e:
            # 先放这个，不能没有显示
            cursor = None
            print("Query Fail", repr(e))
            pass
        if cursor is not None:
            res = cursor.fetchall()
    return res


def FetchAllRoleTypes():
    res = None
    with sql.connect(data_path) as conn:
        try:
            cursor = conn.execute("""
            select * from UserRole
            """)
        except sql.DatabaseError as e:
            # 先放这个，不能没有显示
            cursor = None
            print("Query Fail", repr(e))
            pass
        if cursor is not None:
            res = cursor.fetchall()
    return res


def FetchAllUser():
    res = None
    with sql.connect(data_path) as conn:
        try:
            cursor = conn.execute("""
            select * from User
            """)
        except sql.DatabaseError as e:
            # 先放这个，不能没有显示
            cursor = None
            print("Query Fail", repr(e))
            pass
        if cursor is not None:
            res = cursor.fetchall()
    return res
