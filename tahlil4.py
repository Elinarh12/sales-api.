import pandas as pd

import sqlite3

import matplotlib.pyplot as plt
SELECT city,
SUM(quantity * price) AS sales
FROM orders
GROUP BY city