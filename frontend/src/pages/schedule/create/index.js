import React from "react";
import { Link } from "react-router-dom";
import Header from "../../../components/header";

const ScheduleCreate = () => {
    return (
        <>
            <div className="flex">
                <Header />

                <div className="items-center w-full mx-32">
                    <p className="my-4 px-2 text-2xl font-bold tracking-wider">Create</p>
                    <p className="text-lg py-2 font-medium tracking-wider border-b-4">Schedule</p>

                    <div className="w-1/3 my-4">
                        <p className="text-md font-medium">PaperName</p>
                        <input className="w-full" placeholder="Please input the name..." />
                    </div>

                    <div className="w-1/3 my-4">
                        <p className="text-md font-medium">ExamDate</p>
                        <input className="w-full" placeholder="Please input the name..." />
                    </div>

                    <div className="w-1/3 my-4">
                        <p className="text-md font-medium">ExamTime</p>
                        <input className="w-full" placeholder="Please input the name..." />
                    </div>

                    <div className="w-1/3 my-4">
                        <p className="text-md font-medium">Duration</p>
                        <input className="w-full" placeholder="Please input the name..." />
                    </div>

                    <div className="w-1/3 my-4">
                        <p className="text-md font-medium">Hall</p>
                        <input className="w-full" placeholder="Please input the name..." />
                    </div>

                    <div className="w-1/3 my-4">
                        <p className="text-md font-medium">Exam</p>
                        <input className="w-full" placeholder="Please input the name..." />
                    </div>

                    <div className="w-1/3 my-4">
                        <p className="text-md font-medium">Student</p>
                        <input className="w-full" placeholder="Please input the name..." />
                    </div>

                    <button className="bg-blue-600 text-white py-2 px-4 rounded-lg">Save</button>

                    <div className="pt-2">
                        <Link to="/" className="text-blue-600">Back to List</Link>
                    </div>
                </div>
            </div>
        </>
    )
}

export default ScheduleCreate;