import pandas as pd

import sqlite3

import matplotlib.pyplot as plt
SELECT
strftime('%Y-%m', order_date) AS month,
SUM(quantity * price) AS sales
FROM orders
GROUP BY month
ORDER BY month