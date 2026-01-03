import joblib
# Maan lete hain ke aapka trained model 'rf_model' hai
# Ise save karne ke liye ye code run karen:
joblib.dump(rf_model, 'model.pkl')
print("Model saved as model.pkl successfully!")