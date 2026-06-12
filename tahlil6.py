import pandas as pd

import sqlite3

import matplotlib.pyplot as plt
SELECT customer_id,
COUNT(*) AS total_orders
FROM orders
GROUP BY customer_id