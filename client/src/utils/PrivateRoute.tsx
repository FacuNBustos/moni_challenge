import { Navigate } from 'react-router-dom';

const PrivateRoute = ({ isAuthenticated, children }:any) => {
    return isAuthenticated? children : <Navigate to="/login" />
}

export default PrivateRoute;