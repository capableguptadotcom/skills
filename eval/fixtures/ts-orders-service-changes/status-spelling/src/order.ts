export type OrderStatus = "pending" | "paid" | "cancelled";

export type Order = {
  id: string;
  status: OrderStatus;
  placedAt: Date;
  totalCents: number;
};

export function statusLabel(status: OrderStatus): string {
  switch (status) {
    case "pending":
      return "Awaiting payment";
    case "paid":
      return "Paid";
    case "cancelled":
      return "Cancelled";
    default: {
      const unknown: never = status;
      throw new Error(`unknown status ${unknown}`);
    }
  }
}
