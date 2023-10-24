import { useState } from "react";
import AuthService from "../../services/AuthService";
import { useNavigate } from "react-router-dom";
import User from "../../interfaces/User";

const LoginPage = ({ setUserTokens }:any) => {

  const navigate = useNavigate();
  const [formPayload, setFormPayload] = useState<User>({
    username: "",
    password: ""
  })
  
  const handleChangeFormPayload = (e:any) => {
    setFormPayload((prev:any) => {
      prev[e.target.name] = e.target.value
      return prev
    })
  }

  const handleSubmit = (e:any) => {
    e.preventDefault();
    AuthService.Login(formPayload)
    .then(response => {
      if (response != false) {
        localStorage.setItem("access",response.access)
        localStorage.setItem("refresh", response.refresh)

        setUserTokens({
          access: response.access,
          refresh: response.refresh,
          isAuthenticated: true
        })
        navigate("/backoffice")
      }
    })
  }
  
  return (
    <div className="flex justify-center items-center w-screen h-screen bg-[#B9DFF9]">
      <section className="flex justify-center items-center w-full h-[10rem]">
        <form className="flex flex-col justify-center items-center w-[31rem] h-[30rem] bg-[#F0F6FA] gap-[2%] rounded-xl shadow shadow-gray-300 relative" 
        onChange={e => handleChangeFormPayload(e)}
        onSubmit={(e) => handleSubmit(e)}>
          <p className="absolute top-0 text-[3rem] font-bold text-[#3B82F6]">MONI</p>
          <p className="text-[2rem] font-bold pb-[3%]">Login Administrativo</p>
          <div className="w-[80%]">
            <p className="text-[0.9rem] font-bold pl-[3px]">Usuario</p>
            <input type="text" name="username" className="w-full h-[2.5rem] text-center"/>
          </div>

          <div className="w-[80%]">
            <p className="text-[0.9rem] font-bold pl-[3px]">Contrasenia</p>
            <input type="password" name="password" className="w-full h-[2.5rem] text-center"/>
          </div>
          <button type="submit" className="w-[70%] bg-blue-200 h-[2.5rem] mt-[5%] rounded-full
          hover:bg-blue-300">
            Ingresar
          </button>
        </form>
      </section>
    </div>
  );
};

export default LoginPage;
