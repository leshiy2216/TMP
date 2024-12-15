import csv
import re


regular = [
    r'^[A-Za-z]+$',          
    r'^\d{1,3}$',            
    r'^\d{4}-\d{2}-\d{2}$',  
    r'^\+?\d{10,15}$',       
    r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$',  
    r'^[A-Z]{2}\d{4}[A-Z]{2}$',  
    r'^\d+\.\d{2}$',          
    r'^[A-Z][a-z]+$',        
    r'^[A-Za-z0-9]{8,}$',    
    r'^[A-Za-z\s]+$'         
]


