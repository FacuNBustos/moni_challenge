import { useState } from "react"
import LoanSwiftService from "../../services/LoanSwiftService";
import LoanSwift from "../../interfaces/LoanSwift";
import banner from "../../assets/banner_login.png"
import Validator from "../../utils/Validator";

const LoanSwiftPage = () => {
    const [formPayload, setFormPayload] = useState<LoanSwift>({
        document_number: NaN,
        first_name: "",
        last_name: "",
        gender: "",
        email: "",
        amount: NaN
    });
    const [error, setError] = useState({
        isError: false,
        acceptance: false
    })
    const [success, setSucces] = useState(false);

    const handleChangeFormPayload = (e:any) => {
        setFormPayload((prev:any) => {
            prev[e.target.name] = e.target.value
            return prev
        })
    }

    const handleSubmit = (e:any) => {
        e.preventDefault();
        setError({isError:false, acceptance:false})
        setSucces(false)

        if (Validator.isLoanSwift(formPayload) == false){
            setError((prev) => {
                return {...prev, isError: true}
            })
            return
        };

        LoanSwiftService.create(formPayload)
        .then(response => {
            if (response) {
                setSucces(true)
            }else {
                setError({isError: true, acceptance: true})
            }
        })
    }

    return(
        <div className="grid grid-cols-3 w-screen h-screen">
            <div className="col-span-2">
                <img src={banner} alt="banner" className="h-full"/>
            </div>
            <section className="bg-[#FFFFFF] relative">
                {
                    (error.isError)
                    ? <div className="flex justify-center items-center absolute top-10 w-full h-[6rem]">
                        {
                            (error.acceptance)
                            ?<div className="flex justify-center items-center w-[80%] h-full bg-red-200">
                                <p>Ah ocurrido un problema, intentelo mas tarde</p>
                            </div>
                            :<div className="flex justify-center items-center w-[80%] h-full bg-yellow-200">
                                <p>Error en alguno de los campos ingresados</p>
                            </div>
                        }
                    </div>
                    : null
                }
                {
                    (success)
                    ?<div className="flex justify-center items-center absolute top-10 w-full h-[6rem]">
                        <div className="flex justify-center items-center w-[80%] h-full bg-green-200">
                            <p>{formPayload.first_name} {formPayload.last_name} se le ah otorgado el prestamo</p>
                        </div>
                    </div>
                    :null
                }

                <form onChange={e => handleChangeFormPayload(e)}
                onSubmit={ (e) => handleSubmit(e) }
                className="flex flex-col justify-center items-center h-full bg-[#EFEFEF] gap-[2%]">
                    <div className="w-[60%]">
                        <p className="text-[0.9rem]">Numero de documento</p>
                        <input type="number" name="document_number" className="w-full h-[2rem] text-center"/>
                    </div>
                    <div className="w-[60%]">
                        <p className="text-[0.9rem]">Nombre</p>
                        <input type="text" name="first_name" className="w-full h-[2rem] text-center"/>
                    </div>
                    <div className="w-[60%]">
                        <p className="text-[0.9rem]">Apellido</p>
                        <input type="text" name="last_name" className="w-full h-[2rem] text-center"/>
                    </div>
                    <select name="gender" className="w-[60%] h-[2rem] text-center">
                        <option value="" defaultChecked>Selecciona un genero</option>
                        <option value="Male">Masculino</option>
                        <option value="Female">Femenino</option>
                        <option value="Non-binary">No Binario</option>
                    </select>
                    <div className="w-[60%]">
                        <p className="text-[0.9rem]">Correo Electronico</p>
                        <input type="text" name="email" className="w-full h-[2rem] text-center"/>
                    </div>
                    <div className="w-[60%]">
                        <p className="text-[0.9rem]">Monto del prestamo</p>
                        <input type="number" name="amount" className="w-full h-[2rem]"/>
                    </div>

                    <button className="w-[55%] h-[2rem] bg-blue-200 rounded-full font-bold
                    hover:bg-blue-300">
                        Pedir Prestamo
                    </button>
                </form>
            </section>

        </div>
    )
}

export default LoanSwiftPage