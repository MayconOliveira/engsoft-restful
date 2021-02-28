import logo from './logo.svg';
import './App.css';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faUserEdit,faUserMinus } from '@fortawesome/free-solid-svg-icons'


function App() {
  return (
    <div className="main-content">
      <div className="container mt-5">   
        <h2 className="mb-5">CPF Busca</h2>
        <div className="row align-items-center">
          <div className="col-md-6">
            <input type="text" name="busca" className="form-control" />
          </div>
          
        </div>
        <div className="row">
          <div className="col">
            <div className="card shadow">
              <div className="card-header border-0">
                <h3 className="mb-0">Pessoas</h3>
              </div>
              <div className="table-responsive">
                <table className="table align-items-center table-flush">
                  <thead className="thead-light">
                    <tr>                      
                      <th scope="col">ID</th>
                      <th scope="col">Nome</th>
                      <th scope="col">CPF</th>
                      <th scope="col">Data de Nascimento</th>
                      <th scope="col">Endereço</th>
                      <th scope="col"></th>
                      <th scope="col"></th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      
                      <td>1</td>
                      <td>Maycon</td>
                      <td>125.234.336-42</td>
                      <td>23/12/1993</td>
                      <td>R. Pedro Fontana, 20 - Inhoaíba - Rio de Janeiro - RJ, 23059-090</td>
                      <td><button className="btn btn-primary btn-icon-only"><FontAwesomeIcon icon={faUserEdit} /></button></td>
                      <td><button className="btn btn-danger btn-icon-only"><FontAwesomeIcon icon={faUserMinus} /></button></td>
                    </tr>
                    
                  </tbody>
                </table>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
