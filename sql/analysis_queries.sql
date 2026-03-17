-- Attrition by department
SELECT 
    department,
    COUNT(*) AS employees,
    SUM(attrition_flag) AS employees_left,
    ROUND(AVG(attrition_flag)*100, 2) AS attrition_rate
FROM employees
GROUP BY department;

-- Attrition by tenure
SELECT
    years_at_company,
    ROUND(AVG(attrition_flag)*100, 2) AS attrition_rate
FROM employees
GROUP BY years_at_company
ORDER BY years_at_company;