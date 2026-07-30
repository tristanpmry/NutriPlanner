interface Props {

    title: string;

    children: React.ReactNode;

}


export default function Card(
    { title, children }: Props
) {


    return (

        <div>

            <h2>
                {title}
            </h2>

            <div>
                {children}
            </div>

        </div>

    );

}