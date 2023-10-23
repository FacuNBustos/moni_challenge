import { useEffect, useState } from "react";
import LoanSwiftService from "../../services/LoanSwiftService";
import LoanSwift from "../../interfaces/LoanSwift";
import Validator from "../../utils/Validator";

const BackofficePage = () => {
  const [loanList, setLoanList] = useState([])
  const [isEdit, setIsEdit] = useState<any>({
    status: false,
    elem: {}  
  })

  const handleResetList = () => {
    const token = localStorage.getItem("access");
    if (token) {
      LoanSwiftService.list(token)
      .then(response => setLoanList(response.payload))
    }
  }

  const handleDeleteLoan = (id:string) => {
    const token = localStorage.getItem("access")
    if (token) {
      LoanSwiftService.delete(id, token)
      .then(response => {
        if (response) {
          handleResetList()
        }
      })
    }
  }

  const handleHandleChangeEditCard = (elem:{}) => {
    setIsEdit({status: !isEdit.status, elem:elem})
  }

  const handleSubmitEdit = (e:any) => {
    e.preventDefault()
    const payload:LoanSwift = {
      document_number: isEdit.elem.document_number,
      first_name: e.target.first_name.value,
      last_name: e.target.last_name.value,
      gender: e.target.gender.value,
      email: e.target.email.value,
      amount: e.target.amount.value
    } 
    if (Validator.isLoanSwift(payload) == false){
      return
    };
    const token = localStorage.getItem("access");
    if (token) {
      LoanSwiftService.patch(isEdit.elem.id, payload, token)
      .then(response => {
        if (response) {
          handleHandleChangeEditCard({})
          handleResetList()
        }
      })
    }
  }

  useEffect(()=> {
    handleResetList()
  }, [])


  return(
    <div className="flex justify-center items-center w-screen h-screen bg-[#EFEFEF]">
      {
        (isEdit.status)
        ? <section className="flex justify-center items-center absolute w-screen h-screen bg-white/60"
        onDoubleClick={() => handleHandleChangeEditCard({})}>
          <div className="flex justify-center items-center w-[30%] h-[50%] bg-blue-200 z-10">
            <form className="flex flex-col w-full justify-center items-center gap-3" 
            onSubmit={(e) => handleSubmitEdit(e)}>
              <div className="w-[70%]">
                <p>Numero de documento</p>
                <input type="text" disabled value={isEdit.elem.document_number} className="text-center w-full h-[2rem]"/>
              </div>
              <div className="w-[70%]">
                <p>Nombre</p>
                <input type="text" name="first_name" className="text-center w-full h-[2rem]" defaultValue={isEdit.elem.first_name}/>
              </div>
              <div className="w-[70%]">
                <p>Apellido</p>
                <input type="text" name="last_name" className="text-center w-full h-[2rem]" defaultValue={isEdit.elem.last_name} />
              </div >            
              <select name="gender" className="text-center w-[70%] h-[2rem]" defaultValue={isEdit.elem.gender}>
                <option value="Male">Masculino</option>
                <option value="Female">Femenino</option>
                <option value="Non-binary">No Binario</option>
              </select>
              <div className="w-[70%]">
                <p>Correo Electronico</p>
                <input type="text" name="email" className="text-center w-full h-[2rem]" defaultValue={isEdit.elem.email}/>
              </div>
              <div className="w-[70%]">
                <p>Monto del Prestamo</p>
                <input type="number" name="amount" className="text-center w-full h-[2rem]" defaultValue={isEdit.elem.amount}/>
              </div>
              <button type="submit" className="w-[65%] bg-green-300 h-[2rem] rounded-full
              hover:bg-green-400">
                Editar Registro
              </button>
            </form>
          </div>
        </section>
        : null
      }

      <section className="flex flex-col w-[80%] h-[80%] bg-white overflow-y-scroll gap-[10px]">
        <div className="flex items-center justify-between w-full min-h-[3rem] p-3">
          <p>Numero DNI</p>
          <p>Nombre completo</p>
          <p>Email</p>
          <p>Genero</p>
          <p>Monto prestamo</p>
          <div className="w-[25%]"/>
        </div>
        {
          (loanList.length >= 1)
          ? loanList.map((elem:any, key) => {
            return(
              <div className="flex justify-between items-center w-full min-h-[3.5rem] bg-gray-200 p-3" key={key}>
                <p>{elem.document_number}</p>
                <div className="flex gap-1">
                  <p>{elem.first_name}</p>
                  <p>{elem.last_name}</p>
                </div>
                <p>{elem.email}</p>
                <p>{elem.gender}</p>
                <p>{elem.amount}</p>
                <div className="flex justify-center items-center w-[30%] gap-[1rem]">
                  <button className="bg-blue-200 px-[3rem] py-1 rounded-full
                  hover:bg-blue-300"
                  onClick={ () => handleHandleChangeEditCard(elem) }>
                    Editar
                  </button>
                  <button className="shadow shadow-gray-500 px-[3rem] py-1 rounded-full
                  hover:bg-red-400 hover:text-white"
                  onClick={() => handleDeleteLoan(elem.id)}>
                    Eliminar
                  </button>
                </div>
              </div>
            )
          })
          : null
        }
      </section>
    </div>
  )
};

export default BackofficePage;
