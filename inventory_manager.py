import pandas as pd

# 1. Industrial Resource Database
# We use custom Material IDs and Names to make it professional
plant_data = {
    'Material_ID': ['ST-101', 'CL-205', 'WR-302', 'HO-408', 'SG-510'],
    'Material_Name': ['High-Grade Steel', 'Industrial Coolant', 'Welding Rods', 'Hydraulic Oil', 'Safety Gears'],
    'Current_Stock': [450, 80, 800, 50, 120],
    'Safety_Threshold': [500, 150, 500, 100, 150]
}

# Converting dictionary to a structured table (DataFrame)
df = pd.DataFrame(plant_data)

# 2. Advanced Logic: Detecting items below safety limits
shortage_report = df[df['Current_Stock'] < df['Safety_Threshold']].copy()

print("--- 🏭 INDUSTRIAL RESOURCE MANAGEMENT SYSTEM ---")

if not shortage_report.empty:
    # 3. Calculation: Exactly how much to re-order
    shortage_report['Quantity_to_Order'] = shortage_report['Safety_Threshold'] - shortage_report['Current_Stock']
    
    # 4. Smart Labeling: Setting 'Urgency' status for Management
    # This logic shows that you understand business priorities
    shortage_report['Priority'] = shortage_report['Current_Stock'].apply(
        lambda x: '🚨 CRITICAL' if x < 100 else '⚠️ RE-ORDER'
    )

    # Displaying a clean report for HR/Management
    output = shortage_report[['Material_Name', 'Current_Stock', 'Quantity_to_Order', 'Priority']]
    print("\nURGENT: The following materials require replenishment:")
    print(output.to_string(index=False))
else:
    print("\n✅ All systems stable. Stock levels are optimal.")

# 5. Monitoring Summary
print(f"\nScan complete. Total materials audited: {len(df)}")

