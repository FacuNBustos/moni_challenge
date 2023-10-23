import { Route, Routes } from "react-router-dom";
import HomePage from "./pages/Home/HomePage";
import LoginPage from "./pages/Login/LoginPage";
import PrivateRoute from "./utils/PrivateRoute";
import BackofficePage from "./pages/Backoffice/BackofficePage";
import { useEffect, useState } from "react";
import AuthService from "./services/AuthService";
import LoanSwiftPage from "./pages/LoanSwift/LoanSwiftPage";

function App() {
  const [userTokens, setUserTokens] = useState({
    access: "",
    refresh: "",
    isAuthenticated: false
  });

  useEffect(() => {
    const accessToken = window.localStorage.getItem('access')
    const refreshToken = window.localStorage.getItem('refresh')
    if (accessToken && refreshToken) {
      AuthService.verify(accessToken)
      .then(response => {
        if (response) {
          setUserTokens({
            access: accessToken,
            refresh: refreshToken,
            isAuthenticated: true
          })
        }
      })
    }
  }, [ userTokens.access ])

  return (
    <>
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/loanswift" element={<LoanSwiftPage />} />
        <Route path="/login" element={<LoginPage setUserTokens={setUserTokens} />}/>
        <Route
          path="/backoffice"
          element={
            <PrivateRoute isAuthenticated={userTokens.isAuthenticated}>
              <BackofficePage />
            </PrivateRoute>
          }
        />
      </Routes>
    </>
  );
}

export default App;
