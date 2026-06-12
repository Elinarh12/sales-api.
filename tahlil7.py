import pandas as pd

import sqlite3

import matplotlib.pyplot as plt
SELECT
CASE
WHEN signup_date < '2025-01-01'
THEN 'Before'
ELSE 'After'
END AS period,
COUNT(*) AS total
FROM users
GROUP BY period