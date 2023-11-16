import sqlite3

conn = sqlite3.connect('plasticdb.sqlite3')
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS matdesity (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            material TEXT,
            density_melt REAL,
            density_solid REAL,
            remark TEXT
            ) """)

c.execute("""CREATE TABLE IF NOT EXISTS cushiondatasetting (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            screwdetail TEXT,
            screwsize TEXT,
            cushion TEXT,
            remark TEXT
            ) """)

c.execute("""CREATE TABLE IF NOT EXISTS shearrate (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            material TEXT,
            shear_rate REAL,
            remark TEXT
            ) """)

c.execute("""CREATE TABLE IF NOT EXISTS effective_thermal (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            material TEXT,
            effective_thermal REAL,
            remark TEXT
            ) """)

c.execute("""CREATE TABLE IF NOT EXISTS glass_transition (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            material TEXT,
            glass_transition REAL,
            remark TEXT
            ) """)


c.execute("""CREATE TABLE IF NOT EXISTS productdata (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            product_name TEXT,
            product_weight REAL,
            maetrial TEXT,
            density REAL,
            cavity INTEGER,
            screw_dia REAL,
            volumn_at_melt REAL,
            short_stroke REAL,
            chshion REAL,
            shot_size REAL,
            hold_position REAL, 
            diameter_gate REAL,
            number_of_gate INTEGER,
            shear_rate REAL,
            flow_rate REAL,
            injection_time REAL,
            hold_time_sec REAL,
            hold_time_max REAL,
            hold_time_min REAL,
            injection_speed REAL,
            eff_thermal_diff REAL,
            part_thickness REAL,
            melt_temp REAL,
            mold_temp REAL,
            ejector_temp REAL,
            glass_transition REAL,
            cooling_time REAL,
            remark TEXT
            ) """)


def view_data(table_name):
    with conn:
        command = 'SELECT * FROM {}'.format(table_name)
        c.execute(command)
        result = c.fetchall()
        #count = len(result)
        #for i in range(count):    
        #print(result[i])
    return result
