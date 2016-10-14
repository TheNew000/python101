



cursor.execute("SELECT meta_value, field_id, item_id FROM wp_kczafk_frm_item_metas T1 WHERE (T1.item_id = 1 OR T1.item_id = 2 OR T1.item_id = 3) AND (field_id = 25 OR field_id = 15 OR field_id = 8)")
first_name = cursor.fetchall()
print first_name
cursor.execute("SELECT meta_value, field_id, item_id FROM wp_kczafk_frm_item_metas T1 WHERE (T1.item_id = 1 OR T1.item_id = 2 OR T1.item_id = 3) AND (field_id = 26 OR field_id = 16 OR field_id = 9)")
last_name = cursor.fetchall()
print last_name
cursor.execute("SELECT meta_value, field_id, item_id FROM wp_kczafk_frm_item_metas T1 WHERE (T1.item_id = 1 OR T1.item_id = 2 OR T1.item_id = 3) AND (field_id = 27 OR field_id = 17 OR field_id = 10)")
email = cursor.fetchall()
print email

for i in range (0, len(first_name)):
    cursor.execute("INSERT INTO email_list (id, First_Name, Last_Name, Email, Website, Title, Message) VALUES (%r, %r, %r, %r, %r, %r, %r)", (result[i][0], table_list[0], table_list[1], table_list[2], 'NULL', 'NULL', 'NULL'))
    conn.commit()


for i in range (0, len(result)):
    table_list = result[i][1].split(', ', 5)
    for j in range (0, len(table_list)):
        if table_list[j] is None:
            table_list[j] = 'NULL'
    if len(table_list) < 3:
        print "This Person Sucks"
    elif len(table_list) < 6:
        cursor.execute("SELECT Email FROM email_list WHERE Email = %r", table_list[2])
        email_present = cursor.fetchone()
        if email_present is None:
            cursor.execute("INSERT INTO email_list (id, First_Name, Last_Name, Email, Website, Title, Message) VALUES (%r, %r, %r, %r, %r, %r, %r)", (result[i][0], table_list[0], table_list[1], table_list[2], 'NULL', 'NULL', 'NULL'))
    elif len(table_list) == 6:
        cursor.execute("SELECT Email FROM email_list WHERE Email = %r", table_list[2])
        email_present = cursor.fetchone()
        if email_present is None:
            cursor.execute("INSERT INTO email_list (id, First_Name, Last_Name, Email, Website, Title, Message) VALUES (%r, %r, %r, %r, %r, %r, %r)", (result[i][0], table_list[0], table_list[1], table_list[2], table_list[3], table_list[4], table_list[5]))
    conn.commit()
