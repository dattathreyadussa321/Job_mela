# 🚻 Database Management Guide - Toilets/Restrooms

This guide shows you **3 easy ways** to add and manage toilets in your Job Mela database.

---

## 📌 Method 1: Custom Management Commands (RECOMMENDED ✅)

I've created custom Django commands that make it super easy to manage toilets from the command line.

### **1️⃣ Add a New Toilet**

```bash
python manage.py add_toilet --name "Men's Restroom - Block D" --gender MALE --block D --floor 2
```

**Arguments:**
- `--name` - Name of the restroom (required)
- `--gender` - MALE or FEMALE (required)
- `--block` - Block letter (e.g., A, B, C, D) (required)
- `--floor` - Floor number (e.g., 0, 1, 2) (required)
- `--room` - Room number (optional)

**Examples:**

```bash
# Add a male restroom
python manage.py add_toilet --name "Men's Restroom - Block E Ground Floor" --gender MALE --block E --floor 0

# Add a female restroom with room number
python manage.py add_toilet --name "Women's Restroom - Block F" --gender FEMALE --block F --floor 1 --room "F101"

# Add restrooms for a new block
python manage.py add_toilet --name "Men's Restroom - Block G" --gender MALE --block G --floor 0
python manage.py add_toilet --name "Women's Restroom - Block G" --gender FEMALE --block G --floor 0
```

---

### **2️⃣ List All Toilets**

```bash
# Show all toilets
python manage.py list_toilets

# Filter by gender
python manage.py list_toilets --gender MALE
python manage.py list_toilets --gender FEMALE

# Filter by block
python manage.py list_toilets --block A
```

---

### **3️⃣ Delete a Toilet**

```bash
# First, list toilets to find the ID
python manage.py list_toilets

# Then delete by ID
python manage.py delete_toilet 11
```

---

### **4️⃣ Clear All Toilets**

```bash
# This will delete ALL toilets (requires confirmation)
python manage.py clear_toilets --confirm
```

---

## 📌 Method 2: Django Admin Panel

1. **Start the server** (if not running):
   ```bash
   python manage.py runserver
   ```

2. **Open admin panel**:
   ```
   http://localhost:8000/admin/
   ```

3. **Navigate to**: Companies → Facilities → Add Facility

4. **Fill in the form**:
   - Name: `Men's Restroom - Block D`
   - Location type: **Select "Toilet"** (very important!)
   - Gender: Select "Male" or "Female"
   - Block: `D`
   - Floor: `2`
   - Room number: (optional)

5. **Click "Save"**

6. **Refresh the toilets page** to see changes:
   ```
   http://localhost:8000/toilets/
   ```

**⚠️ Important Notes:**
- Make sure to select **"Toilet"** as the Location type
- Click the **"Save"** button (not "Save and add another")
- Hard refresh your browser (Ctrl + F5) if you don't see changes

---

## 📌 Method 3: Modify the Populate Script

Edit the file `populate_toilets.py` to add your custom toilets:

```python
# Add new toilets to the toilets_data list
toilets_data = [
    {
        'name': 'Men\'s Restroom - Block D',
        'location_type': 'TOILET',
        'block': 'D',
        'floor': 0,
        'gender': 'MALE',
    },
    # Add more toilets here...
]
```

Then run:
```bash
python populate_toilets.py
```

---

## 🔍 Verify Changes

After adding toilets, verify they're saved:

```bash
# Quick check
python manage.py list_toilets

# Detailed database check
python db_test.py

# View on frontend
# Open: http://localhost:8000/toilets/
```

---

## 💡 Quick Examples

### Add toilets for a new block (Block H):

```bash
python manage.py add_toilet --name "Men's Restroom - Block H Ground Floor" --gender MALE --block H --floor 0
python manage.py add_toilet --name "Women's Restroom - Block H Ground Floor" --gender FEMALE --block H --floor 0
python manage.py add_toilet --name "Men's Restroom - Block H First Floor" --gender MALE --block H --floor 1
python manage.py add_toilet --name "Women's Restroom - Block H First Floor" --gender FEMALE --block H --floor 1
```

### Delete all toilets and start fresh:

```bash
python manage.py clear_toilets --confirm
python populate_toilets.py  # Re-populate with default data
```

---

## 📊 Current Database Status

Run this to check current status:

```bash
python manage.py list_toilets
```

---

## ❓ Troubleshooting

### Toilets not showing on frontend?

1. **Hard refresh browser**: Press `Ctrl + F5`
2. **Check database**: `python manage.py list_toilets`
3. **Restart server**: Stop and restart `python manage.py runserver`

### Admin panel save not working?

Use the custom management commands instead - they're more reliable!

---

## 🎯 Recommended Workflow

**For quick changes:**
```bash
python manage.py add_toilet --name "..." --gender MALE --block D --floor 2
python manage.py list_toilets
```

**For bulk additions:**
Edit `populate_toilets.py` and run `python populate_toilets.py`

**For deletions:**
```bash
python manage.py delete_toilet <ID>
```

---

## 📝 Notes

- All changes are **immediate** - no migrations needed
- Changes are **permanent** - stored in `db.sqlite3`
- Frontend updates **automatically** from the database
- Use `list_toilets` to verify changes anytime

---

**Need help?** Run any command with `--help`:

```bash
python manage.py add_toilet --help
python manage.py list_toilets --help
python manage.py delete_toilet --help
```
