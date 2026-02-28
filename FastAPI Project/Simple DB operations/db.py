import sqlite3


class DB:
    def __init__(self):
        self.con = sqlite3.connect("data.db")
        self.cur = self.con.cursor()



    def add_record(self,first_name : str,
                last_name :str ,
                DOB : str,
                phone : str,
                email : str,
                company: str,
                sector: str,
                skills: str):
        
        try:
            self.cur.execute("""
            INSERT INTO profile 
            (first_name, last_name, DOB, phone, email, company, sector, skills)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                first_name,
                last_name,
                DOB,
                phone,
                email,
                company,
                sector,
                skills
            ))
            self.con.commit()
            self.con.close()
            print("Record Inserted Successfully")
        except Exception as e:
            print(f"There is some issue while inserting data {e}")


    def fetch_all(self):
        self.cur.execute("SELECT * FROM profile")
        rows = self.cur.fetchall()
        data = []
        for row in rows:
            data.append(row)

        return {"data": data}


    def fetch_by_id(self, id :int):
        try:
            self.cur.execute(f"SELECT * FROM profile where id = {id}")
            rows = self.cur.fetchall()
            data = []
            for row in rows:
                data.append(row)

            return {"data": data}
        
        except Exception as e :
            print(f"There is some issue while fetching the data : {e}")


    def update_first_name(self, old_first_name :str,
                        new_first_name : str):
        try:
            self.cur.execute("""
                UPDATE profile
                SET first_name = ?
                WHERE first_name = ?
                """, (new_first_name, old_first_name))
            
            self.con.commit()
            self.con.close()
            return "Successfully updated record "
        except Exception as e :
            print(f"There is issue while updating the recrod! {e}")

    def delete_record(self, id: int):
        try:
            self.cur.execute(
                "DELETE FROM profile WHERE id = ?",
                (id,)
            )
            self.con.commit()

            if self.cur.rowcount == 0:
                return {"error": "Record not found"}

            return {"data": "Record Deleted Successfully"}

        except Exception as e:
            return {"error": f"Issue while deleting record: {str(e)}"}


if __name__ == '__main__':
    db_obj = DB()
    # add_record("Rehan", "Aatif", "06-01-1996", "9431950569","md.rehan@gmail.com","WellsFargo", "IT","Python, AWS, GCP, FastAPI")

    # print(db_obj.fetch_by_id(1))
    print(db_obj.fetch_all())
    # print(update_first_name('Rehan', 'Rehaan'))
