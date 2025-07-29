# Smart Inventory Database Q&A 🏪

An intelligent database query system that allows users to interact with a MySQL inventory database using natural language queries. Built with LangChain, Google Gemini AI, and Streamlit.

## 🚀 Features

- **Natural Language Processing**: Ask questions in plain English about your inventory
- **AI-Powered SQL Generation**: Automatically converts natural language to accurate SQL queries
- **Real-time Database Queries**: Executes queries on live MySQL database
- **Indian Market Ready**: Pricing in Indian Rupees (₹800-₹4000 range)
- **Discount Management**: Handles complex discount calculations
- **Few-shot Learning**: Improved accuracy through example-based learning
- **User-friendly Interface**: Clean Streamlit web interface

## 🛠️ Technology Stack

- **Backend**: Python, LangChain, Google Gemini API
- **Database**: MySQL with PyMySQL connector
- **Frontend**: Streamlit
- **Vector Store**: ChromaDB
- **Embeddings**: Hugging Face Sentence Transformers
- **Environment**: Python 3.12+

## 📋 Prerequisites

- Python 3.12+
- MySQL Server
- Google AI API Key
- Conda (recommended) or pip

## 🔧 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/AnshulJn95/Smart-Inventory-Database-QandA.git
cd Smart-Inventory-Database-QandA
```

### 2. Set Up Python Environment
```bash
# Create conda environment (recommended)
conda create -n inventory_qa python=3.12
conda activate inventory_qa

# Or create virtual environment
python -m venv inventory_qa
source inventory_qa/bin/activate  # On Windows: inventory_qa\Scripts\activate
```

### 3. Install Dependencies
```bash
# Install core packages via conda (recommended for avoiding compilation issues)
conda install transformers tokenizers -y

# Install remaining packages via pip
pip install -r requirements.txt
```

### 4. Set Up Environment Variables
Create a `.env` file in the project root:
```env
GOOGLE_API_KEY=your_google_api_key_here
```

### 5. Database Setup
1. Install and start MySQL server
2. Run the database creation script:
```bash
mysql -u root -p < database/db_creation_sample_db.sql
```

## 📦 Dependencies

```txt
langchain==0.3.15
langchain-core==0.3.15
langchain-community==0.3.15
langchain-experimental==0.3.15
langchain-google-genai==2.0.4
langchain-huggingface==0.1.0
python-dotenv==1.0.0
streamlit==1.32.0
protobuf==3.20.3
pymysql==1.1.0
sentence-transformers==2.2.2
chromadb==0.4.24
sqlalchemy==2.0.23
```

## 🗄️ Database Schema

The system uses two main tables:

### `t_shirts` table:
- `t_shirt_id`: Primary key
- `brand`: Van Heusen, Levi, Nike, Adidas
- `color`: Red, Blue, Black, White
- `size`: XS, S, M, L, XL
- `price`: Price in Indian Rupees (₹800-₹4000)
- `stock_quantity`: Available inventory

### `discounts` table:
- `discount_id`: Primary key
- `t_shirt_id`: Foreign key reference
- `pct_discount`: Discount percentage (0-100)

## 🚀 Usage

1. **Start the application:**
```bash
streamlit run main.py
```

2. **Open your browser** and navigate to `http://localhost:8501`

3. **Ask questions** in natural language:
   - "How many total t-shirts are in stock?"
   - "What's the total value of Nike inventory?"
   - "How many white Adidas t-shirts in size L do we have?"
   - "What revenue would we generate selling all Levi's shirts with discounts?"

## 💡 Sample Questions

- **Inventory Queries**:
  - "How many t-shirts do we have left for Nike in XS size and white color?"
  - "How many white color Levi's shirts do I have?"

- **Financial Queries**:
  - "How much is the total price of the inventory for all S-size t-shirts?"
  - "If we sell all Levi's T-shirts today with discounts applied, how much revenue will we generate?"

- **Business Analytics**:
  - "How much sales amount will be generated if we sell all large size t-shirts today in Nike brand after discounts?"

## 🏗️ Project Structure

```
Smart-Inventory-Database-QandA/
├── main.py                     # Streamlit application entry point
├── langchain_helper.py         # Core LangChain integration
├── few_shots.py               # Few-shot learning examples
├── requirements.txt           # Python dependencies
├── .env                       # Environment variables (create this)
├── database/
│   └── db_creation_sample_db.sql  # Database setup script
└── README.md                  # Project documentation
```

## 🔑 Key Components

### **Few-Shot Learning**
The system uses example-based learning with predefined question-SQL-answer triplets to improve query accuracy.

### **Vector Similarity Search**
Uses ChromaDB and sentence transformers to find the most relevant examples for each query.

### **SQL Safety**
- Validates column names against database schema
- Uses parameterized queries to prevent SQL injection
- Limits result sets to prevent excessive resource usage

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request
