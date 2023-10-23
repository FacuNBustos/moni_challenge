import banner from "../../assets/banner.png";
import { useNavigate } from "react-router-dom";

const HomePage = () => {
  const navigate = useNavigate()
  return(
    <div className="flex flex-col w-screen h-screen bg-[#F2F2F2]">
      <header className="flex justify-center items-center gap-[40%] fixed top-0 w-full h-[6rem] bg-white/[60%]">
        <h3 className="text-blue-500 text-[2rem] font-bold">MONI</h3>
        <button className="w-[12rem] h-[3rem] font-bold rounded-xl shadow-sm shadow-gray-400 text-blue-500
        hover:bg-[#659EEA] hover:text-white"
        onClick={() => navigate("/login")}>
          Ingresar
        </button>
      </header>
      <section className="flex items-center h-full w-full">
        <div className="grid grid-cols-2 w-full h-[40rem] bg-[#BFD8F8]" >
          <div className="flex justify-start items-center">
            <img src={banner} alt="banner moni" className="h-full" />
          </div>
          <div className="flex flex-col items-start pl-[5%] pt-[20%]
          [&>p]:text-white [&>p]:font-bold">
            <p className="text-[2rem] h-[2rem] flex items-center">Buenas soy,</p>
            <p className="text-[8rem] h-[8rem] flex items-center">Moni</p>
            <p className="text-[2rem] h-[2rem] flex items-center">Solicita tu prestamo el en acto.</p>
            <div className="flex justify-center items-center w-[50%] pt-[2%]">
              <button className="w-[90%] h-[4rem] bg-[#5493E7] rounded-full text-[1.3rem] text-white"
              onClick={() => navigate("/loanswift")}>
                Solicitar prestamo
              </button>
            </div>
          </div>
        </div>
      </section>
    </div>
  )
};

export default HomePage;
