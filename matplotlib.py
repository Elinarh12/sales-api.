size=(8, 5)) #ساخت صفحه نمودار
        plt.hist(
            df["price"],
            bins=20
        )  #نمودار هیستوگرام برای توزیع قیمت ها در 20 بازه

        plt.title("Price Distribution") #عنوان نمودار
        plt.xlabel("Price") #عنوان محور افقی
        plt.ylabel("Frequency")  #عنوان محور عمودی
        plt.tight_layout()  #تنظیم فاصله اجزای نمودار
        plt.savefig("price_distribution.png") #ذخیره نمودار ب صورت عکس
        plt.show() #نمایش نمودار

    def orders_per_customer(self): #تعداد سفارشهای هر مشتری

        query = """
        SELECT customer_id,
               COUNT(order_id) AS total_orders
        FROM orders
        GROUP BY customer_id
        ORDER BY total_orders DESC
        """  #کاستمرایدی انتخاب و تعداد سفارش ها حساب و در ستونی ک اسم مستعار دادیم میریزه از جدول سفارشات
        #بر اساس مشتری گروهبندی و تعداد سفارش ها ب صورت نزولی مرتب میشه

        df = pd.read_sql(query, self.conn)  #نتیجه در دیتافریم ذخیره میشه

        plt.figure(figsize=(12, 5))  #ساخت صفحه نمودار
        plt.bar(
            df["customer_id"].astype(str),
            df["total_orders"]
        )  #نمودار میله ای عمودی برای هر کاستمرایدی ک چند سفارش داشته

        plt.title("Orders Per Customer") #عنوان نمودار
        plt.xlabel("Customer ID") #عنوان محور افقی
        plt.ylabel("Orders") #عنوان محور عمودی
        plt.xticks(rotation=90) #نوشته های محورافقی 90 درجه بچرخان
        plt.tight_layout() #تنظیم فاصله اجزای نمودار
        plt.savefig("orders_per_customer.png") #ذخیره نمودار ب صورت عکس
        plt.show() #نمایش نمودار

    def customer_behavior(self):  #رفتار خرید مشتری قبل و بعد ثبتنام

        query = """
        SELECT
        CASE
            WHEN o.order_date < u.signup_date
            THEN 'Before Signup'
            ELSE 'After Signup'
        END AS status,
        COUNT(*) AS total_orders
        FROM orders o
        JOIN users u
        ON o.customer_id = u.user_id
        GROUP BY status
        """  #اگر تاریخ سفارش قبل از ثبتنام کاربر باشه یا کوچکتر باشه اون جمله رو نمایش میده در غیر این صورت
        #جمله بعدی رو نمایش میده میریزه داخل ستون اسم مستعار تعداد رکورد ها شمردهاز جدوا سفارشات بعد جوین میده
        #با جدوا کاربرا و هر سفارش به کاربر مربوط ب ان وصل میشه که جدولهای مربوط جدول کاربرا ستون کاستمرایدی با جدول
        #کاربرا ستون یوزرایدی بر اساس وضعیت داده ها گروه بندی میشن یعنی قبل از ثبتنام و بعد از ثبنام 

        df = pd.read_sql(query, self.conn) #نتیجه ها در دیتافریم ذخیره میشن

        plt.figure(figsize=(6, 5)) #ساخت صفحه نمودار
        plt.bar(
            df["status"],
            df["total_orders"]
        )  #نمودار میله ای عمودی برای مقایسه دادهای عددی چند سفارش بعد از ثبتنام و قبل از ثبتنام

        plt.title("Customer Behavior") #عنوان نمودار
        plt.xlabel("Status") #عنوان محور افقی
        plt.ylabel("Orders") #عنوان محور عمودی
        plt.tight_layout() #تنظیم فاصله اجزای نمودار
        plt.savefig("customer_behavior.png") #ذخیره نمودار ب صورت عکس
        plt.show() #نمایش نمودار