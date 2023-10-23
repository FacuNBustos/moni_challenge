import CommonServices from "./CommonServices";
import LoanSwift from "../interfaces/LoanSwift";

class LoanSwiftService extends CommonServices {
    public constructor() {
        super()
    }

    public async create(payload: LoanSwift) {
        try {
            const response = await this.backend_axios.post(
                "loanswift/create/",
                payload
            )
            if (response.status == 201) {
                return true
            }
            return false
        } catch(_err) {
            return false
        }
    }

    public async list(token: string) {
        try {
            const response = await this.backend_axios.get(
                "/loanswift/list/",
                {
                    headers:{
                        "Authorization": `Bearer ${token}`
                    }
                }
            )
            
            if (response.status == 200) {
                return response.data
            }
            return []
        } catch(_err){
            return []
        }
    }

    public async delete(id:string, token:string) {
        try {
            const response = await this.backend_axios.delete(
                `loanswift/delete/${id}/`,
                {
                    headers: {
                        Authorization: `Bearer ${token}`
                    }
                }
            )
            if (response.status == 200) {
                return true
            }
            return false
        }catch(_err) {
            return false
        }
    }

    public async patch(id:string, payload:LoanSwift, token:string) {
        try {
            const response = await this.backend_axios.patch(
                `loanswift/patch/${id}/`,
                payload, {
                    headers: {
                        Authorization: `Bearer ${token}`
                    }
                }
            )
            if (response.status == 200) {
                return true
            }
            return false
        }catch(_err) {
            return false
        }
    }
}

export default (new LoanSwiftService)